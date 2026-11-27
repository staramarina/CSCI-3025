# Tiffany Mui - Module 9 Assignment

An expense tracker that accepts multiple CSV exports from a variety of banks.  

Estimated Minimum: ![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)    
Development Environment: Python 3.14.4

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modules](#modules)
- [Data Files](#data-files)
- [Warnings/Errors](#warnings--errors)
- [Testing](#testing)
- [Author/Credits](#author--credits)

---

## Overview
The personal expense tracker was created for State University of New York (SUNY): Empire State University (ESU), CSCI-3025: Python Programming course as the Module 9 assignment.

The personal expense tracker: 
- TODO (describe flow of main program)

Ground work for the following features is included, but not fully implemented:
- Mixed date formatting flagging - the case of indeterminate day, month, or year first is caught and the user is prompted with a warning. Other mixed date formatting is caught with format="mixed" to avoid warnings from pandas when supporting unexpected date formats. 
- All files provided are assumed to be analyzed as a single data set, however, this can be changed to support multiple separate or combined data sets with only changes within the main program, since analysis is conducted per class instance. 
- Informational messages are not logged to keep log size relatively small. 

## Features
- Robust error and warning handling with timestamped logging of both.
- Informative warnings print to the console and allows the user to select whether they want to proceed.
- Fairly bank format agnostic file input: only a date column and amount, debit, or credit column is required for basic analysis.

## Installation

### Prerequisites
- Python 3.11 or higher (estimated)
- External Packages
    - pandas - handles data formatting and analysis
    - numpy - handles additional data formatting
    - seaborn - creates graphs
    - matplotlib - handles the underlying settings for graphs

### Setup Steps
1. Download the repository from https://github.com/staramarina/CSCI-3025/tree/main/Module9
2. Verify all files and folders are present
```
   Module9/
    ├── charts                          # Empty directory to hold generated charts
    ├── Mui_Ancillary.py                # General purpose ancillary tools
    ├── Mui_IO.py                       # Handles all input/output for the program
    ├── Mui_M9Assignment.py             # Main program
    ├── Mui_Parser.py                   # Normalizing and transforming CSVs to pandas dataframes
    └── Mui_Statement.py                # Class for bank statements, analysis, and chart generation
```
3. Install pandas package: (note: it is recommended to utilize a virtual environment to segment dependencies)
```
python -m pip install pandas
```
4. Install seaborn package:
```
python -m pip install seaborn
```
5. Ensure numpy is installed. It usually installs alongside pandas, but if it didn't, run the following command:
```
python -m pip install numpy
```
6. Ensure matplotlib is installed. It usually installs alongside seaborn, but if it didn't, run the following command:
```
python -m pip install matplotlib
```
7. Ensure Python path includes the Module9 directory or run from within it.

## Usage

### Running the Program
From the Module9 directory  
```python Mui_M9Assignment.py```

### Example Interaction
```
TODO
```

### Example Chart Generation
TODO

## Project Structure
```
   Module9/
    ├── Mui_Ancillary.py                      # General purpose ancillary tools
    ├── Mui_IO.py                             # Handles all input/output for the program
    ├── Mui_M9Assignment.py                   # Main program
    ├── Mui_Parser.py                         # Normalizing and transforming CSVs to pandas dataframes
    ├── Mui_Statement.py                      # Class for bank statements, analysis, and chart generation
    ├── pyproject.toml                        # Project configuration file
    ├── README.md                             # Read me file (current file)
    ├── charts                                # Directory to hold generated charts
    │   ├── bal_chart.png                     # Example line chart of maximum balance per day
    │   ├── cat_chart.png                     # Example bar chart of total expenses by category
    │   ├── descript_chart.png                # Example bar chart of total expenses by description
    │   ├── spend_chart.png                   # Example line chart of aggregate expenses per day
    │   └── top5_chart.png                    # Example pie chart of top 5 expenses
    ├── tests                                 # Test files for unittest
    │   ├── __init__.py                       # Tells Python this is a package
    │   ├── test_ancillary.py                 # Tests for Mui_Ancillary.py
    │   ├── test_io.py                        # Tests for Mui_IO.py
    │   ├── test_parser.py                    # Tests for Mui_Parser.py
    │   └── test_statement.py                 # Tests for Mui_Statement.py
    └── data                                  # Data used for manual tests
        ├── bofa_checking_example.csv         # Estimated example of checking account export from Bank of America
        ├── chase_checking_example.csv        # Estimated example of checking account export from Chase
        ├── chase_credit_example.csv          # Estimated example of credit card account export from Chase
        ├── citibank_checking_example.csv     # Estimated example of checking account export from Citibank
        ├── citibank_credit_example.csv       # Estimated example of credit card account export from Citibank
        ├── sample-bank-transactions.csv      # Sample generic bank export from https://getutilly.com/guides/sample-bank-statement-csv
        ├── SCU_checking_example.csv          # Example of checking account export from SAFE Credit Union
        ├── SCU_credit_example.csv            # Example of credit card account export from SAFE Credit Union
        ├── USAA_checking_example.csv         # Example of checking account export from USAA
        └── USAA_credit_example.csv           # Example of credit card account export from USAA
```

## Modules

### Built-in Packages
- sys for graceful program exits
- copy to make deep copies without affecting original instances
- datetime for representing dates
- logging to support error and warning logging
- re to support matching shapes

### External Packages
- pandas for handling large data formatting and analysis
    - Estimated Minimum: 2.0
    - Development Environment: 3.1.1
- seaborn for creating graphs
    - Estimated Minimum: 0.13
    - Development Environment: 0.13.2
- matplotlib for handling graph input
    - Estimated Minimum: 3.7
    - Development Environment: 3.11.2
- numy for handling data formatting
    - Estimated Minimum: 1.20.3
    - Development Environment: 2.5.5

### Ancillary Module (Mui_Ancillary.py)
| Function | Purpose | Return |
| ----- | ------ | ------ |
| int_check(num_str) | Determines whether a string can be converted to an integer | (True, int) on success, otherwise (False, error message) |

### XXX Module (Mui_XXX.py)
| Function | Purpose | Return |
| ----- | ------ | ------ |
TODO

## Data Files
A set of test files is included within the data folder. The examples from USAA and SAFE Credit Union (SCU) were based off real exports and utilize the observed formats, headers, and leading/trailing rows. The examples from Bank of America (BofA), Chase, Citibank, and Wells Fargo were estimated based on information available; as such, the format of the data from these banks may differ from the examples. Checking and savings accounts appeared to share formats, but differed in formatting between checking and credit cards. An example of each was included from the pool of sample banks with the exception of Wells Fargo and BofA credit cards, as there was not enough information available to determine the formatting at a confidence rating of at least 50%. Sample transaction data within these files are based on real, but sanitized, transactions. 

In addition to the generated sample data, a generic "sample-bank-transactions.csv" was obtained from https://getutilly.com/guides/sample-bank-statement-csv. This file was also used for testing purposes. 

Other files tested, but not included within the data folder, were real, but anonymized, transaction data for a period of 18 months from USAA and SCU. While the data is anonymized, it does include purchase habits, balance information, etc.; because the GitHub repository is public, the full data set is not published. 

### Verification Rules
The expense tracker has robust data validation and parsing rules as described in the following sections. 

#### File Input
- Files are input via terminal user interface by specifying the path and name with extension
- Input files must be in CSV format
- Data validation on the contents of the file can detect the following
    - Header row at row 0
    - Missing header row
    - Leading rows above the header that contain less than 3 commas (user must remove leading rows if they have 3 or more commas)
    - Assumes that there is a minimum of 4 data columns (user must add addition columns if less than 4, though they can be completely blank)
- Files that do not exist, exist but are empty, have malformed data, or result in other value errors will generate a notification to the terminal and log the full details of the error. 

#### Data Parsing
- The parser module will attempt to detect the date format with the following rules/assumptions.
    - Separating characters are used and include "/" or "-"
    - Dates are not of formats YY-MM-DD, YY/MM/DD, YY-DD-MM, YY/DD/MM, i.e. if the year is first it must be 4 digits followed by month, then day.
    - If the year is last as either YYYY or YY, a check is run to determine whether the day is first or not. In an ambiguous case, the assumption is made that month is first (most common in the U.S.) and the user is prompted to approve this assumption. Example: 10/11/12 is interpreted as 11 Oct 2012.
    - Mixed formatting, e.g. MM/DD/YYYY and MM-DD-YY within the same column are handled via pandas format="mixed", but position order must be consistent, i.e. cannot swap between MM/DD/YY and DD/MM/YY. While this fallback is slower, especially in cases that do not need it, it prevents excessive trace back warnings in the console. Masking the warning was considered, but there was a concern that additional masking would result as well as the thread-safety of conducting this. Ultimately, the design decision was made to avoid these concerns with a slight decrease in performance. 
- CSVs with missing header row is accepted, but the following assumptions are made. The operator must approve the action before the assumed header row is added.
    - There is a minimum of one and a maximum of two date columns. The first being for "Date" or "Transaction Date", the second being for "Posted Date"
    - There is a minimum of one and a maximum of three money/float type columns. 
        - If one is present, it is assumed to be "Amount" with mixed positive and negative numbers. 
        - If two are present, a check is run to determine if the combination is "Debit", "Credit" or "Amount", "Balance". If there is any instance of values in both columns within the row, then the latter is assumed. Otherwise the former is assumed.
        - If three are present, it is assumed to be "Debit", "Credit", and "Balance"
- The parser assumes the following.
    - All rows must have a "Date" value, though "Post Date" may be omitted.
    - Any instance of "bal" represents "Balance", e.g. Running bal., Balance, etc.
    - Any instance of "debit" represents "Debit", e.g. Debit, Amount Debit
    - Any instance of "credit" represents "Credit", e.g. Credit, Amount Credit
    - Any instance of "amount" other than those listed above represents "Amount"
    - An "Amount" column must be present
The parser also handles the following.
    - If both "Debit" and "Credit", but not "Amount" are present, "Debit" and "Credit" are merged into a single "Amount" column
    - If only "Debit" or "Credit" is present, but not "Amount", the column is renamed as "Amount"
    - Fully empty/NA columns are removed

Consistent signage on "Amount" values - For banks with "Debit" and "Credit" columns, the standard that expenses are negative and credits are positive is enforced. However, there is no method for determining the convention when a single "Amount" column is given. The convention varies between banks and in the case of USAA, depends on the account type. No assumption is made when performing the analysis, though it does result in negative numbers appears in charts. TODO verify this when the charts are built.


## Warnings & Errors
- The following are warnings and can be overridden via the console if the user chooses.
    - Ambiguous dates detected, will assume month first if operator selects "Y"/"y", otherwise exit.
    - Missing column header information detected, will infer if operator selects "Y"/"y", otherwise exit.
    - If converting money columns to float data-type fails, the column can be skipped if operator selects "Y"/"y", otherwise exit.
    - If a file could not be converted to a pandas data frame, the operator is given the option to skip that file with "Y"/"y", otherwise exit.
    - If data parsing/cleaning fails on a single pandas data frame, the operator can continue with the next with "Y"/"y", otherwise exit.
- The following are errors that cannot be overridden. The program will gracefully exit. 
    - TODO
- Exceptions to the behavior above are as follows.
    - An error is generated when inputting a file fails, so a generic error is given. However, the operator can try the file input again.
    - If all files could not be converted to a pandas data frame, the operator is notified and the program exits. Additional logs are not generated, as each instance was already logged. 
    - If all data frames fail data parsing/cleaning, the operator is notified and the program exists. Additional logs are not generated, as each instance was already logged. 
- Other warning and error information includes the following.
    - All warnings and errors are logged in a file.
    - Warnings inform the user what happened and give an option to proceed.
    - Errors provide generic information in the console with details in the logs.


## Testing

### Manual Testing
Manual testing included utilizing examples provided in the data folder as well as real (though sanitized) exports from USAA and SAFE Credit Union (full data was not published due to privacy, but may be provided upon request). Each section of the main program prior to the analysis section was tested and dumped to the "test_dump.txt" file. This process can be recreated using the following steps. 

1. Insert the following code between the import section and the main section
```
TEST_FILES = {
    'data/bofa_checking_example.csv': True,
    'data/chase_checking_example.csv': True,
    'data/chase_credit_example.csv': True,
    'data/citibank_checking_example.csv': True,
    'data/citibank_credit_example.csv': True,
    'data/sample-bank-transactions.csv': True,
    'data/SCU_checking_example.csv': True,
    'data/SCU_credit_example.csv': True,
    'data/USAA_checking_example.csv': True,
    'data/USAA_credit_example.csv': True,
    'data/wellsfargo_checking_example.csv': True
}
```
2. Comment the "Ask user for their transaction files" section by adding three double quotes (""") at the beginning and another three (""") at the end.
3. Change line "for file in file_list:" to "for file in TEST_FILES:".
4. Enter the following code between "Build dataframes from CSV files" and "Parse/clean dataframes".
```
    with open('test_dump.txt', "w") as f: 
        f.write('------------------------ORIGINAL DATAFRAMES------------------------\n')
        for df in df_list.values():  # pre-cleaning print
            f.write(df.to_string(header=True, index=True))  # dumps data to file
            f.write('\n\n')  # extra lines for readability
```
5. Enter the following code between "Parse/clean dataframes" and "Create a list of statement class instances".
```
    with open('test_dump.txt', "a") as f: 
        f.write('------------------------CLEAN DATAFRAMES------------------------\n')
        for df in df_clean.values():  # pre-classes print
            f.write(df.to_string(header=True, index=True))  # dumps data to file
            f.write('\n\n')  # extra lines for readability
```
6. Enter the following code between "Create a list of statement class instances" and "Add all class instances together into a single class instance".
```
    with open('test_dump.txt', "a") as f: 
        f.write('------------------------CLASSES------------------------\n')
        for data in df_class:  # post-classes print
            f.write(str(data))  # dumps data to file
            f.write('\n\n')  # extra lines for readability
```
7. Enter the following code between "Add all class instances together into a single class instance" and "Analysis"
```
    with open('test_dump.txt', "a") as f: 
        f.write('------------------------COMBINED------------------------\n')
        f.write(str(all_data))  #post combined print
```

TODO add remaining manual test steps, include manual end-to-end test

### Automated Testing
All test cases are compatible with both unittest and pytest. All 134 test cases pass with both pytest and unittest.  
To run all tests with unittest, enter the following from within the Module9 directory.
```
python -m unittest
```
To run all tests with pytest, enter the following from within the Module9 directory.
```
python -m pytest
```

#### Ancillary Module Tests (test_ancillary.py)
| Class | Method | Purpose |
| ----- | ------ | ------ |
| TestIntCheck(unittest.TestCase) |  | Class to test the int_check(num_str) function |
|  | test_valid_num(self) | Tests various valid integers |
|  | test_null_input(self) | Tests function with missing input |
|  | test_char_input(self) | Tests function with character/string input |
|  | test_decimal_input(self) | Tests function with decimal number input |

#### Specific Module Tests (test_XXX.py)

##### Testing Fixtures, Variables, and Functions
| Type | Name | Purpose |
| ----- | ------ | ------ |
TODO

##### Testing Classes & Methods
| Class | Method | Purpose |
| ----- | ------ | ------ |
TODO

## Author & Credits
Author: Tiffany M. Mui  
Institution: State University of New York: Empire State University  
Course: CSCI-3025 - Python Programming  
Instructor: Dr. Sahand Ziabari  
Date: XX Nov 2026  

### Tools & AI Use Disclosure
- Black 26.10.1 was utilized to ensure PEP8 compliance. All changes were manually reviewed and approved/disapproved as appropriate.
- Proton Lumo 2.0 was utilized as a search engine and included the following tasks:
	- Researching consumer CSV export header formats and column structures for Chase, Bank of America, Wells Fargo, and Citibank.
	- Explaining package function behaviors, e.g. how pandas evaluates to_datetime when performed at the column level and what it does when there is not a consistent format.
	- Various syntax clarification, e.g. what is the syntax to determine whether any value within a pandas dataframe column matches a regex shape.

### Resources & References
- Utilly. (2026). Free sample bank statement CSV (fictional, with known totals). https://getutilly.com/guides/sample-bank-statement-csv
