import xlsxwriter

def write_rule_testcases(filename, inputcols, agg_tests):
    pass


def create_workbook(filepath, header_cols):
    workbook = xlsxwriter.Workbook(filepath)
    worksheet = workbook.add_worksheet()

    for colno, header in enumerate(header_cols):
        worksheet.write(0, colno, header)
    
    return workbook, worksheet



def write_preprocess_testcases(filepath, headercols, output_agg):
    workbook = xlsxwriter.Workbook(filepath)
    worksheet = workbook.add_worksheet()

    for col_no, header in enumerate(headercols):
        worksheet.write(0, col_no, header)

    
    for row_no, row_data in enumerate(output_agg, 1):
        
        for col_no, cell_data, in enumerate(row_data):
            print("==================\n")
            print(cell_data)
            print(type(cell_data))
            worksheet.write(row_no, col_no, cell_data)

    workbook.close()