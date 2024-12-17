## L6 - DE Drudgery

### Setting up the repository
1. Clone the repository
2. [Create and activate an environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) for the project using a package of your choice (venv or conda)
3. Install requirements with 
```pip install -r requirements. txt ```

### Processing Rule Workflows
The file ``rule_parser.py`` prompts you to create a file for each specific column in a
rule. You can fill in this column by copy pasting the data from the Jira ticket. 

Then the script prompts you to go through each row, for each of the columns you specified, line by line. (If show_data configuration option is true in ``rule_parser.py``). The line is automatically copied to your clipboard. 

This option can be disabled if you only want to generate test cases. 

Then the script will generate test cases and write them into a file. This is coordinated using ``process_data, generate_test_cases, write_rule_testcases`` functions. View the source code for the configuration options available.  

Finally, the script will print out the comment you need to write down when completing the ticket, in Markdown format. This is also automatically copied to your clipboard.

Limitations:
- For numerical values, test cases are only generated with ints
- Test cases for the default case are not generated (coming soon!)
- Be sure to enter valid data to the data files for the test cases to pass. Makes sure the OutomeMessage file does not contain quotes, since the lookup matrix does not expect quotes when evaluating test cases.
- Each test case is generated independently. So, some testcases may be caught by a previous condition. You will have to manually edit these test cases to meet the specific condition only

#### Instructions to use

1. In `rule_parser.py`, add INPUT_COLS,OUTPUT_COLS, FOLDER_NAME as per the example format
2. Configure options in file as necessary
3. Run ```python rule_parser.py```

### Preprocess Workflows Test case Generation

The tool can generate your SIT ENV Test case.xlsx file as well as the general test case file. 
To do so, modify the params under main to match the relevant workflow
(PROCESS_WF_NAME, WF_VERSION, WF_REVISION, USER_ID, RAW_INPUTS)

Then you will have to modify the mapping logic where you map your RAW INPUTS to the application data schema format. 

Once that is done, simply run ``python preprocess.py``

