''' 
Generating testcases for Rules
'''
import random
import utils.utils as utils

print_chosen = lambda index, options, choice : print(f'{index}. Options: {options}, Chosen: {choice}')

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
            choice = random.choice(data_options)
        else:
            # All other rows should contain only one option
            choice = data_options[0]

        # Add string quotes
        choice = f'"{choice}"'
        tests.append(choice)
        if verbose: 
            print_chosen(ind, data_options, choice)

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
            if verbose:
                print_chosen(ind, data_options, choice)
            continue
            
        option = data_options[0]
        
        # Handle ANY
        if utils.find_any(option):
            choice = random.randint(MIN_VALUE, MAX_VALUE)
            tests.append(choice)
            if verbose: 
                print_chosen(ind, data_options, choice)
            continue

        option = int(option) # Option must be number

        if operator == "==":
            choice = option
        elif operator == "<=": 
            choice = random.randint(option, MAX_VALUE)
        elif operator == ">=":
            choice = random.randint(MIN_VALUE, option)
        elif operator == ">":
            choice = random.randint(MIN_VALUE, option-1)
        elif operator == "<":
            choice = random.randint(option + 1, MAX_VALUE)

        tests.append(choice)
        if verbose: 
            print_chosen(ind, data_options, choice)

    return tests

