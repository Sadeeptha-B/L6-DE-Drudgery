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