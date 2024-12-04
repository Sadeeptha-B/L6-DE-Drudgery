from enum import Enum
import os
from rule_testcase_generator import generate_test_case
from excel_writer import write_to_file


'''
Reads relevant file for the specified column and returns
string formatted and non-formatted outputs
'''
def prep_rows(filename, colname, coltype, operator):
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
                formatted_rows.append(format_str(colname, coltype, tmp_list, operator))
                
                tmp_list = []
            else: 
                tmp_list.append(line)

    return formatted_rows, data_rows


def format_str(colname, coltype, elems, operator):
    # Handle ANY
    if len(elems) == 1 and elems[0] in ('ANY', '"ANY"', "'ANY'"):
        return elems[0]

    # Preprocessing - Check if string contains "" or ''
    if coltype == ColType.STRING:
        str_contains_quotes = lambda s : len(s) != 0 and s[0] in ("'", '"') and s[len(s)-1] in ("'", '"')
        
        elems = [e if str_contains_quotes(e) else f'"{e}"' for e in elems]

    out = [f'{colname} {operator} {e}'.strip() for e in elems]
    return ' or '.join(out)
   

'''
For a given column, interactively outputs the data for the column row by row. At the end of iteration returns the
aggregated data arrays for the output
'''
def interactive_output(filename, colname, coltype, operator):
    print(f"{colname}\n=========")
    formatted_arr, data_arr = prep_rows(filename, colname, coltype, operator)
    for index, elem in enumerate(formatted_arr, 1):
        input(f'{index}. {elem}')
    return data_arr


#  Execution
#  =============================================
def create_files(inputcols, outputcols):
    for elem in [*inputcols, *outputcols]:
        colname = elem[0] if isinstance(elem, list)  else elem

        filepath = get_filepath_from_colname(colname)
        if not os.path.exists(filepath):
            open(filepath, 'w').close()
            input(f"{colname}.txt: Please fill in the file ")


def process_data(cols, isOutputCols=False, generate_testcases=True):
    agg_tests = []
    # Do not generate tests for output cols
    generate_testcases = generate_testcases and not isOutputCols 

    for elem in cols:
        if isinstance(elem, list):
            colname, coltype, operator, *_ = elem + [None]*3
            operator = operator or "=="
        else:
            colname, coltype, operator = elem, ColType.STRING, "=="

        filepath = get_filepath_from_colname(colname)
        displayColname, displayOperator = colname, operator

        # Output cols should not display colname and operator
        if isOutputCols:
            displayColname, displayOperator = "", ""
       
        data_arr = interactive_output(filepath, displayColname, coltype, displayOperator)
        
        if generate_testcases:
            # Generate test cases for column
            tests = generate_test_case(colname, coltype, data_arr, operator)
            agg_tests.append(tests)
            

    # Aggregate test cases and write to excel file
    # Prompt for excel file name
    if generate_testcases:
        write_to_file('', cols, agg_tests)
    


if __name__ == "__main__":
    class ColType(Enum):
        STRING = 1
        NUMBER = 2
        BOOLEAN = 3

    FOLDER_NAME = 'data'
    INPUT_COLS = [
        "SubType", 
        "BrandGroup", 
        ["LoanTenor", ColType.NUMBER, "<="],  
        ["IsHasNCB", ColType.BOOLEAN],
        "NCBGrade",
        ["BalloonPaymentAmount", ColType.NUMBER, ">"],
        ["IsTruck", ColType.BOOLEAN],
        "TestProgramCode",
        "CarBrand",
        "CarModel",
        "MCSPAGrade",
        "DealerGroup", 
        ["TestPolicyTighten", ColType.BOOLEAN],
        "CarBrandGroup"
    ]

    OUTPUT_COLS = [
        ["Return", ColType.NUMBER]
    ]

     # Create folder if not exists
    os.makedirs(FOLDER_NAME, exist_ok=True)
    folder_path = os.path.join(os.getcwd(), FOLDER_NAME)
    get_filepath_from_colname = lambda colname : os.path.join(folder_path, f'{colname}.txt')

    create_files(INPUT_COLS, OUTPUT_COLS)

    # Inputs
    process_data(INPUT_COLS)

    # Outputs
    process_data(OUTPUT_COLS, isOutputCols=True, generate_testcases=False)
    