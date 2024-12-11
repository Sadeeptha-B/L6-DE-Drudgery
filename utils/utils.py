import os

def camelcase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]


def find_any(input): 
    return input in ('ANY', '"ANY"', "'ANY'")

'''
For a file nested in a subdirectory in cwd
'''
def get_filepath(folderpath, filename): 
    return os.path.join(os.getcwd(), folderpath, filename)

def str_contains_quotes(s):
    quotes = ("'", '"')
    return len(s) != 0 and s[0] in quotes and s[len(s)-1] in quotes

def strip_quotes(s):
    return s[1:len(s)-1] if str_contains_quotes(s) else s

def add_quotes_if_not_exist(s):
    return s if str_contains_quotes(s) else f'"{s}"'