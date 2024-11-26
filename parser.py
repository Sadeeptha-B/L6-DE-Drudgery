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

    # TODO: Add coltype handling logic
    out = [f'{colname} {operator} {e}'.strip() for e in elems]
    return ' or '.join(out)
   

def interactive_output(filename, colname, coltype, operator):
    print(f"{colname}\n=========")
    output_arr = prep_rows(filename, colname, coltype, operator)
    for elem in output_arr:
        input(elem)


if __name__ == "__main__":
    filename = "data.txt"

    class ColType(Enum):
        STRING = 1
        NUMBER = 2
        BOOLEAN = 3

    input_cols = [
        "SubType", 
        "BrandGroup", 
        ["LoanTenor", "<="],
        "IsHasNCB",
        "NCBGrade",
        ["BalloonPaymentAmount", ">"],
        "IsTruck",
        "TestProgramCode",
        "CarBrand",
        "CarModel",
        "MCSPAGrade",
        "DealerGroup", 
        "TestPolicyTighten",
        "CarBrandGroup"
    ]

    output_cols = ["Return.txt"]
    # Assuming windows machine
    get_filepath_from_colname = lambda colname : f'.\\data\\{colname}.txt'


    # Create files if not exist
    for elem in input_cols.extend(output_cols):
        colname = elem[0] if isinstance(elem, list)  else elem

        filepath = get_filepath_from_colname(colname)
        if not os.path.exists(filepath):
            open(filepath, 'w').close()
            input(f"{colname}.txt: Please fill in the file")


    # Inputs
    for elem in input_cols:
        if isinstance(elem, list):
            colname, operator = elem
        else:
            colname = elem
            operator = "=="

        filepath = get_filepath_from_colname(colname)
        interactive_output(filepath, colname, ColType.STRING, operator)

    # Outputs
    for colname in output_cols:
        filepath = get_filepath_from_colname(colname)
        interactive_output(filepath, "", ColType.NUMBER, "")
