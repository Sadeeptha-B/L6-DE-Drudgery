from enum import Enum
import os

def prep_rows(filename, colname, coltype, operator):
    out = []

    with open(filename) as file:
        tmp_list = []
        for line in file:
            line = line.rstrip("\n")
            if line == "":
                out.append(format_str(colname, coltype, tmp_list, operator))
                tmp_list = []
            else: 
                tmp_list.append(line)

    return out


def format_str(colname, coltype, elems, operator):
    # Handle ANY
    if len(elems) == 1 and elems[0] in ('ANY', '"ANY"', "'ANY'"):
        return elems[0]

    # Preprocessing - Check if string contains "" / ''
    if coltype == ColType.STRING:
        str_contains_quotes = lambda s : len(s) != 0 and s[0] in ("'", '"') and s[len(s)-1] in ("'", '"')
        
        elems = [e if str_contains_quotes(e) else f'"{e}"' for e in elems]

    out = [f'{colname} {operator} {e}'.strip() for e in elems]
    return ' or '.join(out)
   

def interactive_output(filename, colname, coltype, operator):
    print(f"{colname}\n=========")
    output_arr = prep_rows(filename, colname, coltype, operator)
    for index, elem in enumerate(output_arr, 1):
        input(f'{index}. {elem}')


#  Execution
#  =============================================
def create_files(inputcols, outputcols):
    for elem in [*inputcols, *outputcols]:
        colname = elem[0] if isinstance(elem, list)  else elem

        filepath = get_filepath_from_colname(colname)
        if not os.path.exists(filepath):
            open(filepath, 'w').close()
            input(f"{colname}.txt: Please fill in the file ")

            
def process_inputs(inputcols):
     for elem in inputcols:
        if isinstance(elem, list):
            colname, coltype, operator, *_ = elem + [None]*3
            operator = operator or "=="
        else:
            colname = elem
            coltype = ColType.STRING
            operator = "=="

        filepath = get_filepath_from_colname(colname)
        interactive_output(filepath, colname, coltype, operator)


def process_outputs(outputcols):
    for colname in outputcols:
        filepath = get_filepath_from_colname(colname)
        interactive_output(filepath, "", ColType.NUMBER, "")


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

    OUTPUT_COLS = ["Return"]

     # Create folder if not exist,  Assuming windows machine
    os.makedirs(FOLDER_NAME, exist_ok=True)
    get_filepath_from_colname = lambda colname : os.path.join(os.getcwd(), FOLDER_NAME, f'{colname}.txt')

    create_files(INPUT_COLS, OUTPUT_COLS)

    # Inputs
    process_inputs(INPUT_COLS)

    # Outputs
    process_outputs(OUTPUT_COLS)
    
