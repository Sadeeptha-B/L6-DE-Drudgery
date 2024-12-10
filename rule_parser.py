from enum import Enum
import os
from rule_workflows.rule_testcase_generator import generate_non_numerical_testcases, generate_numerical_testcases
from utils.excel_writer import write_rule_testcases as write_to_file
import utils.utils as utils
import pyperclip

# Constants
class ColType(Enum):
    STRING = 1
    NUMBER = 2
    BOOLEAN = 3

DEFAULT_NUM_COL_RANGE = [0,100]


'''
Reads relevant file for the specified column and returns
string formatted and non-formatted outputs
'''
def prep_rows(filename, colname, coltype, operator, is_output_cols=False):
    formatted_rows, data_rows = [], []

    with open(filename) as file:
        tmp_list = []
        for line in file:
            line = line.rstrip("\n")
            if line == "":
                if len(tmp_list) == 0:
                    tmp_list.append('ANY')
                    continue
                
                # Aggregate data
                data_rows.append(tmp_list)
                formatted_rows.append(format_str(colname, coltype, tmp_list, operator, is_output_cols))
                
                tmp_list = []
            else: 
                tmp_list.append(line)

    return formatted_rows, data_rows


def format_str(colname, coltype, elems, operator, is_output_cols=False):
    # Handle ANY
    if len(elems) == 1 and utils.find_any(elems[0]):
        return elems[0]

    # Preprocessing - Check if string contains "" or ''
    # Do not add quotes if output_col
    if coltype == ColType.STRING and not is_output_cols:       
        elems = [e if utils.str_contains_quotes(e) else f'"{e}"' for e in elems]

    out = [f'{colname} {operator} {e}'.strip() for e in elems]
    return ' or '.join(out)
   

'''
For a given column, outputs the data for the column row by row if interactive
'''
def interactive_output(colname, formatted_arr):
    print(f"{colname}\n=========")
    for index, elem in enumerate(formatted_arr, 1):
        pyperclip.copy(elem)
        input(f'{index}. {elem}')


def extract_col_data(col_data):
    if isinstance(col_data, list):
        colname, coltype, operator, min_max, *_ = col_data + [None]*3
        operator = operator or "=="
        min_max = min_max or DEFAULT_NUM_COL_RANGE if coltype == ColType.NUMBER else None 
    else:
        colname, coltype, operator, min_max = col_data, ColType.STRING, "==", None

    return colname, coltype, operator, min_max


# Lots of room for improving this using numpy and pandas dataframes
def postprocess_testcases(cols, agg_tests):
    rows = []

    for row_data in zip(*agg_tests):
        row_dict = {}
        for ind, elem in enumerate(row_data):
            colname, _, _, _ = extract_col_data(cols[ind])
            row_dict[colname] = elem
        rows.append(row_dict)

    return rows  


#  Execution
#  =============================================
def create_files(inputcols, outputcols):
    for elem in [*inputcols, *outputcols]:
        colname = elem[0] if isinstance(elem, list)  else elem

        filepath = get_filepath_from_colname(colname)
        if not os.path.exists(filepath):
            open(filepath, 'w').close()
            input(f"{colname}.txt: Please fill in the file ")


def process_data(cols, show_data=True, is_output_cols=False):
    agg_data_arr = []

    for col_data in cols:
        colname, coltype, operator, _ = extract_col_data(col_data)
        filepath = get_filepath_from_colname(colname)
        displayColname, displayOperator = colname, operator

        # Output cols should not display colname and operator
        if is_output_cols:
            displayColname, displayOperator = "", ""
       
        formatted_arr, data_arr = prep_rows(filepath, displayColname, coltype, displayOperator, is_output_cols)
        agg_data_arr.append(data_arr)
        
        if show_data:
            interactive_output(displayColname, formatted_arr)

    return agg_data_arr


def generate_test_cases(cols, agg_data_arr, verbose_tests=False, postprocess=True):
    agg_tests = []

    # Generate and aggregate test cases
    for col_data, data_arr in zip(cols, agg_data_arr):
        colname, coltype, operator, min_max = extract_col_data(col_data)

         # Generate test cases for column
        if coltype != ColType.NUMBER:
            tests = generate_non_numerical_testcases(colname, coltype, data_arr, verbose=verbose_tests)
        else:
            tests = generate_numerical_testcases(colname, data_arr, operator, min_max, verbose=verbose_tests)
        agg_tests.append(tests)
    
    if postprocess:
        tests_dict = postprocess_testcases(cols, agg_tests)
        return agg_tests, tests_dict 
    return agg_tests, None


def write_rule_testcases(inputcols, outputcols, agg_tests, output_agg, filepath):
    # Preparing headers
    header_cols = ["*execute dm_DecisionMatrix"]
    inputs_formatted = [f'input.{utils.camelcase(extract_col_data(col_data)[0])}' for col_data in inputcols]
    outputs_formatted = [f"expected.*dm_DecisionMatrix.output.{extract_col_data(col_data)[0]}" for col_data in outputcols]
    header_cols.extend([*inputs_formatted, *outputs_formatted])
    header_cols.append("expected.*dm_DecisionMatrix.matchedRow")

    # Preparing data
    # Assumes output_agg data is the data_arr result from process_data directly
    output_agg = [[outrow[0] for outrow in outcol] for outcol in output_agg]
    row_count = len(output_agg[0])
    output_agg.append([i for i in range(1, row_count + 1)])
    data_agg = [*agg_tests, *output_agg]

    write_to_file(filepath, header_cols, data_agg)

if __name__ == "__main__":
    # Example
    # Cols Format - Name, Type, Operator, Min Max range to be used for numerical types
    # When specifying the min, max range be careful to choose two values that are not
    # part of the input dataset. 
    # ======================================================
    #
    # FOLDER_NAME = 'example'
    # INPUT_COLS = [
    #     "SubType", 
    #     "BrandGroup", 
    #     ["LoanTenor", ColType.NUMBER, "<=", [50, 100]],  
    #     ["IsHasNCB", ColType.BOOLEAN],
    #     "NCBGrade",
    #     ["BalloonPaymentAmount", ColType.NUMBER, ">", [-1,10]],
    #     ["IsTruck", ColType.BOOLEAN],
    #     "TestProgramCode",
    #     "CarBrand",
    #     "CarModel",
    #     "MCSPAGrade",
    #     "DealerGroup", 
    #     ["TestPolicyTighten", ColType.BOOLEAN],
    #     "CarBrandGroup"
    # ]
    # OUTPUT_COLS = [
    #     ["Return", ColType.NUMBER]
    # ]
    
    FOLDER_NAME = 'data'
    WF_NAME = 'UW_GuarantorKYC3_Auto'
    INPUT_COLS = [
        "KYCLevel",
        "KYCReason",
        "Occupation",
        "KYCLevelRM",
        "KYCReasonRM",
    ]
    OUTPUT_COLS = [
        ["Return", ColType.BOOLEAN],
        "OutcomeMessage"
    ]

     # Create folder if not exists
    os.makedirs(FOLDER_NAME, exist_ok=True)
    get_filepath_from_colname = lambda colname : utils.get_filepath(FOLDER_NAME, f'{colname}.txt')
    create_files(INPUT_COLS, OUTPUT_COLS)

    '''
    Process Data
    ------------------------
    show_data: Whether to show interactive output (Go over row by row by column by pressing enter)
               You can disable this mode if you only want to generate test cases
    is_output_cols: Output cols do not need boolean expressions. So, this param is used to identify these.
    
    Generate Test cases 
    -------------------------
    verbose_tests: Print detailed outputs for tests
    postprocess: Will return an output dict which aggregates the results row by with each column being a key
    '''
    # Process inputs and outputs
    agg_data_arr = process_data(INPUT_COLS, show_data=False)
    output_agg = process_data(OUTPUT_COLS, show_data=True, is_output_cols=True)
    
    # Test cases
    agg_tests, _= generate_test_cases(INPUT_COLS, agg_data_arr, verbose_tests=True, postprocess=False)

    # Write tests to file
    testcase_filepath = utils.get_filepath(FOLDER_NAME, f'{WF_NAME}_vo_Testing_Review.xlsx')
    write_rule_testcases(INPUT_COLS, OUTPUT_COLS, agg_tests, output_agg, testcase_filepath)