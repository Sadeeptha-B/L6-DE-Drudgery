''' 
Generating testcases for Rules
'''
import random
import utils.utils as utils
from utils.types import ColType
import utils.utils as utils


# Column cell can contain either String, Boolean or Any
def generate_non_numerical_testcases(colname, coltype, data_arr, verbose=True):
    if verbose: 
        print(f"\nGenerating Test Cases for {colname}\n=====================")

    tests = []
    for ind, data_options in enumerate(data_arr, 1):
        if len(data_options) == 0:
            raise ValueError('Each row should have at least one data option')
        
        # Must be a string
        if len(data_options) > 1:
            option = random.choice(data_options)
            choice = option if utils.str_contains_quotes(option) else f'"{option}"'
            tests.append(f'"{choice}"')
            debug_print(ind, data_options, choice, verbose)
            continue

        # All other rows should contain only one option
        option = data_options[0]

        # Handle boolean for ANY
        if utils.find_any(option):
            if coltype == ColType.BOOLEAN:
                choice = random.choice(['true', 'false'])
                tests.append(choice)
                debug_print(ind, data_options, choice, verbose)
                continue

        # Must be string
        choice = option if coltype == ColType.BOOLEAN or utils.str_contains_quotes(option) else f'"{option}"'
        tests.append(choice)
        debug_print(ind, data_options, choice, verbose)

    return tests


# Column cell can contain either Number or Any
# Current implementation only generates ints
def generate_numerical_testcases(colname, data_arr, operator, min_max, verbose=True):
    if verbose: 
        print(f"\nGenerating Test Cases for {colname}\n=====================")
    
    MIN_VALUE, MAX_VALUE = min_max

    tests = []
    for ind, data_options in enumerate(data_arr, 1):
        if len(data_options) == 0:
            raise ValueError('Each row should have at least one data option')
        
        # Handle multiple options
        if len(data_options) > 1:
            # Must be equality
            choice = int(random.choice(data_options))
            tests.append(choice)
            debug_print(ind, data_options, choice, verbose)
            continue
            
        option = data_options[0]
        
        # Handle ANY
        if utils.find_any(option):
            choice = random.randint(MIN_VALUE, MAX_VALUE)
            tests.append(choice)
            debug_print(ind, data_options, choice, verbose)
            continue

        option = int(option) # Option must be number

        if operator == "==":
            choice = option
        elif operator == "<=": 
            choice = random.randint(MIN_VALUE, option)
        elif operator == ">=":
            choice = random.randint(option, MAX_VALUE)
        elif operator == ">":
            choice = random.randint(option + 1, MAX_VALUE)
        elif operator == "<":
            choice = random.randint(MIN_VALUE, option-1)

        tests.append(choice)
        debug_print(ind, data_options, choice, verbose)

    return tests



def debug_print(index, options, choice, verbose):
    if verbose:
        print(f'{index}. Options: {options}, Chosen: {choice}')