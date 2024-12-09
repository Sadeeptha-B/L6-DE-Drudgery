import os

def camelcase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]


def find_any(input): 
    return input in ('ANY', '"ANY"', "'ANY'")

# def get_filepath_from_colname(colname): 
#     return os.path.join(folder_path, f'{colname}.txt')