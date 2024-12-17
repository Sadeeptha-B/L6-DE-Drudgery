import requests
from datetime import date
from utils.excel_writer import write_preprocess_testcases
import json
import os
import pyperclip


'''
Receives application data from ADW and the raw inputs. This is the mapping function to prepare the data
for the relevant workflow. You should change this mapping logic per workflow as per your needs. 
'''
def preprocess_data(application_data, raw_inputs):
    processed_input = []

    for input in raw_inputs:
        copy = json.loads(json.dumps(application_data)) # Deep copy dictionary
        systemverifies = copy["applicationDetails"]["systemverifies"]
        verify = systemverifies[0]
        cdd = verify["appl_systemverify_cdds"][0]
        cdd["appl_systemverify_cdd_alerts"][0]["message"] = input["bklType"]
        processed_input.append(copy)

    return processed_input


def trigger_decision_engine(input_arr):
    wf_name, wf_version, wf_revision, external_id, data_input, http_headers = input_arr

    #TODO- Error handling
    response = requests.post(
        f'https://ms.nleadsdev.se.scb.co.th/runtime/api/process?workflowType=Process&workflowName={wf_name}&workflowVersion={wf_version}&workflowRevision={wf_revision}&externalId={external_id}&externalSystemCode=ms-invoke&settingsProfile=Default&uiRequest=true&scriptingRuntime=',
        headers=http_headers,
        json= data_input
    )

    return response.json()


def generate_output(index, concise_input, response_json):
    request_id, workflow_output = response_json["RequestId"], response_json["WorkflowOutput"]
    bre_records_out = {"breRecords":  list(map(lambda record: {"return": record["return"], "outcomeMessage":record["outcomeMessage"]},
                                                workflow_output["breRecords"]))}
    
    # prettified json inputs and outputs
    in_json = json.dumps(concise_input, indent=4)
    out_json = json.dumps(workflow_output, indent=4)
    bre_records_out_json = json.dumps(bre_records_out, indent=4)
    print(f"Test case {index}\n========================\nInput:", in_json, "\n==================\nOutput:", bre_records_out_json)


    url = f'https://console.nleadsdev.se.scb.co.th/#/report/modern/process/{request_id}?workspace=default'
    return [index, in_json, out_json, bre_records_out_json, url]

def generate_jira_markdown(wf_name, wf_revision):
    print("\nGenerating Jira Output Markdown\n======================================")
    url = f'https://console.nleadsdev.se.scb.co.th/#/workflows/edit/{wf_name}/0/{wf_revision}?workspace=default'
    st = f'**Test Cases - Process WF - [{wf_name}]({url})**\nTest cases -\nProof video -\nSIT ENV Test Cases -'
    pyperclip.copy(st)
    print(st)

# Execution 
# ==========================================================================================
'''
Executing workflow to get data from ADW
'''
def get_input_data(input_arr):
    base_wfname, base_wfversion, base_wfrevision, user_id, auth_token, application_input, raw_inputs, *_= input_arr + [None]*3

    while True:
        res = input(f"Please validate the ADW Data workflow:\n===================================\nWF Details :{base_wfname}\\{base_wfversion}\\{base_wfrevision}")
        if res == "y":
            break

    http_headers, external_id = setup_params(auth_token, user_id)

    rsp_json = trigger_decision_engine([base_wfname, base_wfversion, base_wfrevision, external_id, application_input, http_headers])
    workflow_output = rsp_json["WorkflowOutput"]

    # Data mapping logic - Change per wf
    processed_input = preprocess_data(workflow_output, raw_inputs)
    return processed_input

'''
General workflow execution
'''
def orchestrate_execution(input_arr, generate_testcases=True):
    wf_name, version, revision, user_id, inputs, auth_token, excel_folder, *_= input_arr + [None]*3
    concise_inputs, processed_inputs = inputs

    while True:
        res = input(f"\nPlease validate the Preprocess wf data:\n===================================\nWF Details :{wf_name}\\{version}\\{revision}\nInputs:\n{json.dumps(concise_inputs, indent=4)}")

        if res == "y":
            break
    
    http_headers, external_id = setup_params(auth_token, user_id)
    output_agg = []

    for row_no, proc_input in enumerate(processed_inputs):
        concise_input = concise_inputs[row_no]
        resp_json= trigger_decision_engine([wf_name, version, revision, external_id, proc_input, http_headers])
    
        # Format output
        index, in_json, out_json, bre_records_out_json, url = generate_output(row_no + 1, concise_input, resp_json)
        
        # Write first case to SIT ENV file
        if row_no == 0 and generate_testcases:
            sit_header_cols = ["Process WF Test Case No", "Input Summary", "Input", "Expected output", "Recieved Output", "Report Link [DEV ENV]"]
            filepath = os.path.join(os.getcwd(), excel_folder, 'SIT ENV Test case.xlsx')
            record = [index, in_json, json.dumps(proc_input, indent=4), bre_records_out_json, out_json, url]
            write_preprocess_testcases(filepath, sit_header_cols, [record])


        # Excel header cols expect this format
        output_agg.append([index, in_json, bre_records_out_json, url])

    if generate_testcases:
        agg_header_cols = ['Test Case No', 'Input', 'Output', f'Report Link for {wf_name} [DEV ENV]']
        filepath = os.path.join(os.getcwd(), excel_folder, f'TestCase-{wf_name}.xlsx')
        write_preprocess_testcases(filepath, agg_header_cols, output_agg)
        generate_jira_markdown(wf_name, revision)

    return output_agg

def setup_params(auth_token, user_id):
    http_headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': auth_token,
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'expires': '0',
        'origin': 'https://console.nleadsdev.se.scb.co.th',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://console.nleadsdev.se.scb.co.th/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'zworkspace': 'default',
    }
    external_id = f"{user_id}-{date.today()}"
    return http_headers, external_id


if __name__ == "__main__": 
    # CONSTANTS
    PROCESS_WF_NAME = 'UW_CDDUnsecured_Preprocess'
    WF_VERSION=0
    WF_REVISION=7
    USER_ID='sadeepthab'
    FOLDERNAME = 'data'
    RAW_INPUTS = [{'bklType': "Hit on AMLO Freeze04 List"}, {'bklType': "Hit on AMLO High Risk List"}, {'bklType': "Hit on WORLDCHECK"}, {'bklType': "string"}]
    
    # EPHYMERAL CONSTANTS (Changing per execution)
    AUTH_TOKEN='Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJfcXFNcnNjMGZ2YmlOVFkxVGMtSEJQX2tpLVpwSDZ3X0R0SGJONVFMcnBjIn0.eyJleHAiOjE3MzQ0MDA1MDYsImlhdCI6MTczNDM3NTc1NiwiYXV0aF90aW1lIjoxNzM0MzY0NTA2LCJqdGkiOiJjNWRjMTc2Mi1lNzA5LTRkYTUtOTEwYS05NmIyNDgxZGJmNDQiLCJpc3MiOiJodHRwczovL2tleWNsb2FrLm5sZWFkc2Rldi5zZS5zY2IuY28udGgvcmVhbG1zL25sZWFkcy1kZXYiLCJhdWQiOlsibXMta2V5Y2xvYWsiLCJiYWNrb2ZmaWNlIiwiYWNjb3VudCJdLCJzdWIiOiJjOGRkOTdkYS05ZmFkLTRmOGItODI3YS1kMDE1MWIzYWE4MDQiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJjb25zb2xlIiwic2lkIjoiNjc5ZWE5NDctYjBjNS00NDdiLTgyNDctNWU2YWE4OGJkMTgyIiwiYWNyIjoiMCIsInNjb3BlIjoiZW1haWwgZGF0YXByb3ZpZGVycyBvcGVuaWQgbW9kZWxzIHByb2ZpbGUgYWNyIGNvbmZpZ3VyYXRpb25BcGkgYXVkaXQgdXNlcmRhdGEiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInJvbGUiOlsiRGVjaXNpb25FbmdpbmVXb3JrZmxvd0VkaXRvciIsImRlZmF1bHQtcm9sZXMtbWFzdGVyIiwiR3JhZmFuYUFkbWluaXN0cmF0b3IiLCJEZWNpc2lvbkVuZ2luZVByb3RlY3RlZERhdGFWaWV3ZXIiLCJBRFdBZG1pbmlzdHJhdG9yIiwiRGVjaXNpb25FbmdpbmVSZXBvcnRWaWV3ZXIiLCJEZWNpc2lvbkVuZ2luZVJlY292ZXJ5TWFuYWdlciIsIkRlY2lzaW9uRW5naW5lQXVkaXRWaWV3ZXIiLCJBZG1pbmlzdHJhdG9yIiwiRGVjaXNpb25FbmdpbmVXb3JrZmxvd1NpZ25lciIsIkRlY2lzaW9uRW5naW5lV29ya2Zsb3dFeGVjdXRvciIsIm9mZmxpbmVfYWNjZXNzIiwiQk9Vc2VyIiwidW1hX2F1dGhvcml6YXRpb24iLCJEZWNpc2lvbkVuZ2luZVdvcmtmbG93Vmlld2VyIl0sIm5hbWUiOiJzYWRlZXB0aGFiIiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2FkZWVwdGhhYiJ9.WVjpISue5yKfQ8_qbjkH7Sav5GH8RdbnPUJisvlxL7pQix6ic9ZvCRzQRyHLzViDuxIlWg0UItBDW5ktHMiZa3hPf2NtmPLu-lE9sXz3rzhFKqA95ckB_bxdnL7cUs5dPgdEISnACitF-N53hlKt6AWvOU7XWjZu8JG2Jw2-DsR0SGQ136dm0EB1gifREOOWAJVngMLS9f1sJ-vgNP8OEZBppUGIksyYdfWut-i9XzrymJ7KM3FWAFcDevWE1EYS8yKrGQ_k50T16tlj0wE8wlnc1PHB1eHKG-dT0pujGYvfvfaB0M7-C71klfQ_NotVFl0qXEucvcH0cJLvBs4uxg'

    # # Fetch data from ADW, called base wf
    processed_inputs = get_input_data(['NGL_AutoProcess_GetDependentADWData', 0, 230, USER_ID, 
                                            AUTH_TOKEN, {"applicationId": "APP191000101V"}, RAW_INPUTS])
    
    
    inputs = [RAW_INPUTS, processed_inputs]
    orchestrate_execution([PROCESS_WF_NAME, WF_VERSION, WF_REVISION, USER_ID, inputs, AUTH_TOKEN, FOLDERNAME], RAW_INPUTS)

    generate_jira_markdown(PROCESS_WF_NAME, WF_REVISION)
    







