from enum import Enum
import os
from rule_testcase_generator import generate_non_numerical_testcases, generate_numerical_testcases
from excel_writer import write_rule_testcases
import utils


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
    if len(elems) == 1 and utils.find_any(elems[0]):
        return elems[0]

    # Preprocessing - Check if string contains "" or ''
    if coltype == ColType.STRING:
        str_contains_quotes = lambda s : len(s) != 0 and s[0] in ("'", '"') and s[len(s)-1] in ("'", '"')
        
        elems = [e if str_contains_quotes(e) else f'"{e}"' for e in elems]

    out = [f'{colname} {operator} {e}'.strip() for e in elems]
    return ' or '.join(out)
   

'''
For a given column, outputs the data for the column row by row if interactive
At the end of iteration returns the aggregated data arrays for the output
'''
def interactive_output(colname, formatted_arr):
    print(f"{colname}\n=========")
    for index, elem in enumerate(formatted_arr, 1):
        input(f'{index}. {elem}')


def extract_col_data(col_data):
    min_max = None

    if isinstance(col_data, list):
        colname, coltype, operator, min_max, *_ = col_data + [None]*3
        operator = operator or "=="
        min_max = min_max or DEFAULT_NUM_COL_RANGE # Only considered for numerical types
    else:
        colname, coltype, operator = col_data, ColType.STRING, "=="

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
        colname, coltype, operator, min_max = extract_col_data(col_data)
        filepath = get_filepath_from_colname(colname)
        displayColname, displayOperator = colname, operator

        # Output cols should not display colname and operator
        if is_output_cols:
            displayColname, displayOperator = "", ""
       
        formatted_arr, data_arr = prep_rows(filepath, displayColname, coltype, displayOperator)
        agg_data_arr.append(data_arr)
        
        if show_data:
            interactive_output(displayColname, formatted_arr)

    return agg_data_arr


def generate_test_cases(cols, agg_data_arr, verbose_tests=False, write_to_file=True):
    agg_tests = []

    for col_data, data_arr in zip(cols, agg_data_arr):
        colname, coltype, operator, min_max = extract_col_data(col_data)

         # Generate test cases for column
        if coltype != ColType.NUMBER:
            tests = generate_non_numerical_testcases(colname, coltype, data_arr, verbose=verbose_tests)
        else:
            tests = generate_numerical_testcases(colname, data_arr, operator, min_max, verbose=verbose_tests)
        agg_tests.append(tests)

    # Aggregate test cases and write to excel file
    # Prompt for excel file name    
    if write_to_file:
        write_rule_testcases('', cols, agg_tests)
    
    tests_dict = postprocess_testcases(cols, agg_tests)
    return tests_dict 


if __name__ == "__main__":
    class ColType(Enum):
        STRING = 1
        NUMBER = 2
        BOOLEAN = 3

    FOLDER_NAME = 'data'
    DEFAULT_NUM_COL_RANGE = [0,100]

    #Example
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
    
    INPUT_COLS = [
        ["KYCLevel", ColType.NUMBER, "==", [2,5]],
        ["KYCReason", ColType.NUMBER, "==", [300,325]],
        ["Occupation", ColType.NUMBER, "==", [40,100]],
        ["KYCLevelRM", ColType.NUMBER, "==", [2,5]],
        ["KYCReasonRM", ColType.NUMBER, "==", [300,325]],
    ]


    OUTPUT_COLS = [
        ["Return", ColType.BOOLEAN]
    ]

     # Create folder if not exists
    os.makedirs(FOLDER_NAME, exist_ok=True)
    folder_path = os.path.join(os.getcwd(), FOLDER_NAME)
    get_filepath_from_colname = lambda colname : os.path.join(folder_path, f'{colname}.txt')

    create_files(INPUT_COLS, OUTPUT_COLS)

    '''
    Control panel
    ==============================================
    show_data: Whether to show interactive output (Go over row by row by column by pressing enter)
               You can disable this mode if you only want to generate test cases
    is_output_cols: Output cols do not need boolean expressions. So output cols is used to identify these.
    '''
    # Inputs
    agg_data_arr = process_data(INPUT_COLS, show_data=False)
    tests = generate_test_cases(INPUT_COLS, agg_data_arr, verbose_tests=True, write_to_file=True)
    print(tests)
    
    # Outputs
    process_data(OUTPUT_COLS, show_data=False, is_output_cols=True)
