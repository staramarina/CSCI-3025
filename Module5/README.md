# Tiffany Mui - Module 5 Assignment

A personal budgeting tool that calculates monthly budget information from income and expense data files.

Estimated Minimum: ![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)  
Development Environment: Python 3.14.4

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modules](#modules)
- [Input File Format](#input-file-format)
- [Testing](#testing)
- [Author/Credits](#author--credits)

---

## Overview
The personal budgeting tool was created for State University of New York (SUNY): Empire State University (ESU), CSCI-3025: Python Programming course as the Module 5 assignment. 

The budgeting tool:
- Reads income and expense data from Comma Separated Values (CSV) formatted text files
- Verifies data quantity and type and handles errors gracefully
- Converts payment frequencies (semiannually, quarterly, monthly, weekly, etc.) to annual values
- Calculates income and expenses at monthly rates with percentage of income used
- Results are output via persistent file ('budget_data.txt')

## Features
- **Varying Transaction Occurrence** - Accounts for real-world varying frequencies: yearly, semiannually, quarterly, monthly, bimonthly, weekly, and daily
- **Percentage Calculation** - Calculates and provides percentage of each line item (both income and expenses) relative to total income
- **Persistent Output File** - Output data is appended to a file and can be reviewed at any time
- **Error Handling** - Catches file not found, permission errors, and malformed data
- **Data Verification** - Catches instances of too much and too little data per line from the input files, invalid transaction frequencies, non-numerical data, and duplicate entries

## Installation

### Prerequisites
- Python 3.6 or higher (estimated)
- No external dependencies: required modules are either included or use built-in packages.

### Setup Steps
1. Download the repository from https://github.com/staramarina/CSCI-3025/tree/main/Module5
2. Verify all files are present
```
    Module5/
    ├── Mui_M5Assignment.py     # Main program
    ├── MuiIO.py                # I/O module
    ├── Mui_M5Calculations.py   # Calculations module
    └── TestData/               # Example input files
        ├── IncomeData.txt
        └── ExpenseData.txt
```
3. Ensure Python path includes the Module5 directory or run from within it.

## Usage

### Running the Program
From the Module5 directory  
```python Mui_M5Assignment.py```

### Example Interaction
```
Welcome to Tiffany Mui's Budgeting Tool!
Please enter the file name (with extension) that contains your income data
TestData/IncomeData.txt
Please enter the file name (with extension) that contains your expense data
TestData/Expense.txt
File printed successfully as budget_data.txt
```

### Sample Output File (budget_data.txt)
```
Income 1, 7342.36, 80.24
Income 2, 1808.45, 19.76
Rent, 2384.56, 26.06
Car, 152.45, 1.67
Electricity, 214.89, 2.35
Water, 39.74, 0.43
Internet, 104.49, 1.14
Phone, 39.04, 0.43
Groceries, 510.13, 5.57
```
Report data is rounded to the nearest cent for readability. Full precision data is maintained within program memory.

## Project Structure
```
Module5/
    ├── pyproject.toml              # Project configuration file
    ├── Mui_M5Assignment.py         # Main program (orchestrates workflow)
    ├── MuiIO.py                    # I/O module (file handling and verification)
    ├── Mui_M5Calculations.py       # Calculations module (calculations and data verification)
    ├── TestData/                   # Example input files
    │   ├── IncomeData.txt          # Example income data
    │   └── ExpenseData.txt         # Example expense data
    ├── tests/                      # Test files for pytest
    │   ├── __init__.py             # Tells Python this is a package
    │   ├── conftest.py             # Shared test fixtures
    │   ├── test_io.py              # Tests for MuiIO.py
    │   └── test_calculations.py    # Tests for Mui_M5Calculations.py
    └── README.md                   # Read me file (current file)
```

## Modules

### Built-in Packages
- decimal.Decimal - Precise financial calculations, avoid floating-point errors
- copy - Deep copies used to prevent unintended mutations of original data

### I/O Module (MuiIO.py)
| Function | Purpose | Return |
| -------- | ------- | ------ |
| file_exists(file_name) | Checks if a file can be opened and read | (bool, str) - success flag, message |
| can_write_file(file_name) | Checks if a file can be appended | (bool, str) - success flag, message |
| print_new_file(data_dict) | Prints a dictionary to an existing file (will create if not present) | (bool, str) - success flag, message |

### Calculations Module (Mui_M5Calculations.py)
| Function | Purpose | Return |
| -------- | ------- | ------ |
| generate_budget_object(file_name) | Generates a budget object, can be used for income and expenses | dict - {line number : data list} |
| check_budget_data(budget) | Checks that the amount and type of data is correct | dict - {line number : data list} (removed lines with reason) |
| format_budget_data(budget_raw) | Prepares budgetary data for calculations | dict - {name : [frequency, amount]} |
| yearly_conversion(budget) | Calculates yearly values for income and expenses | dict - {name : [yearly_amount]} |
| sum_income(income) | Calculates total yearly income | Decimal - sum of all income sources |
| budget_calc(budget, total_income = 1) | Calculates monthly income, expenses, and percentages | dict - {name : [monthly_amount, percentage]} |
| budget_rounding(budget) | Rounds all decimal values for report purposes | dict - {name : [monthly_amount, percentage]} |


## Input File Format
Each line in the input file must contain three coma-separated values:  
Item Name, Frequency, Dollar Amount

### Valid Frequency Values
| Frequency | Annual Multiplication |
| -------- | ------- |
| yearly | 1 |
| semiannually | 2 |
| quarterly | 4 |
| monthly | 12 |
| bimonthly | 24 |
| weekly | 52.143 |
| daily | 365.2425 |

### Example Input File (IncomeData.txt)
```
Income 1, bimonthly, 3671.18
Income 2, monthly, 1808.45
```

### Verification Rules
- Exactly 3 comma-separated values per line (blank lines are stripped)
- Frequency value must match one from the list
- Dollar amount must be a valid decimal number
- Item names must be unique across each file

## Testing

### Manual Testing
Run the program with provided test data:  
```python Mui_M5Assignment.py```  
Enter: ```TestData/IncomeData.txt```  
Enter: ```TestData/ExpenseData.txt```

### Automated Testing
Automated tested with pytest. //add more detail later

#### Test Fixtures (conftest.py)
| Function | Purpose |
| -------- | ------- |
| sample_income_file(temp_path) | Creates temporary sample income file and data |
| sample_expense_file(temp_path) | Creates temporary sample expense file and data |
| valid_budget_data(temp_path) | Creates temporary 'good' budget data of mixed frequencies |
| invalid_budget_data(temp_path) | Creates temporary 'bad' budget data |
| sample_income_dict() | Income dictionary as generated by generate_budget_object() |
| sample_format_income() | Formatted income as generated by format_budget_data() |
| sample_yearly_income() | Income converted to yearly values as generated by yearly_conversion() |

#### Calculations Tests (test_calculations.py)
| Class | Method | Purpose |
| ------- | ------- | ------- |
| TestGenerateBudgetObject | | Tests the generate_budget_object() function|
| | test_generate_structure(self, valid_budget_data) | Calls and checks generate_budget_object() |
| | test_empty_file(self, temp_path) | Tests that empty file will return an empty dictionary |
| TestCheckBudgetData | | Tests the check_budget_data() function |
| | test_valid_data_return(self, sample_income) | Tests that valid data will return empty removed lines dictionary |
| | test_wrong_length(self) | Tests that lines of wrong length are flagged and listed |
| | test_invalid_frequency(self) | Tests that invalid frequencies are flagged and listed |
| | test_invalid_amount(self) | Tests that dollar amounts are flagged and listed |
| | test_none_amount(self) | Tests that dollar amount of none is flagged and listed |
| | test_duplicate_name(self) | Tests that invalid frequencies are flagged and listed |
| TestFormatBudgetData | | Tests the format_budget_data function |
| | test_frequency_case(self) | Tests that frequency matching is not case sensitive |
| | test_calc_multiplier(self, sample_income) | Tests that frequencies are converted to numerical multipliers |
| | test_convert_decimal(self, sample_income) | Tests that the dollar amounts convert to decimals |
| TestYearlyConversion | | Tests the yearly_conversion function |
| | test_keys(self, sample_format_income) | Tests that keys remain unchanged after calculations |
| | test_yearly_conversion(self, sample_format_income) | Tests that dollar amounts are calculated to yearly values |
| TestSumIncome | | Tests the sum_income function |
| | test_sum_all_income(self, sample_yearly_income) | Tests that all income sources are added |
| | test_empty_income(self) | Tests that empty income returns Decimal(0) |
| TestBudgetCalc | | Tests the budget_calc function |
| | test_monthly_div() | Tests that yearly amounts are divided by 12 as expected |
| | test_percent_cal() | Tests that percentages are performed as (item / yearly_total) x 100 |
| | test_percent_sum() | Tests that the sum of all percentages is approximately 100% |
| TestBudgetRounding | | Tests the budget_rounding function |
| | test_round_two() | Tests that values are rounded as strings with two decimal places |
| | test_string_output() | Tests that the output is of string type, not Decimal |
| TestEdgeCases | | Tests additional edge cases |
| | test_large_num() | Tests that large numbers can maintain precision |
| | test_small_round() | Tests that small numbers are rounded properly |

#### Input/Output Tests (test_io.py)
| Class | Method | Purpose |
| ------- | ------- | ------- |
| TestFileExists | | Tests the file_exists function |
| | test_file_exists_true(self, temp_path) | Tests that (True, message) is returned when file exists |
| | test_file_not_exists(self) | Tests that (False, message) is returned when file does not exist |
| | test_directory(self, temp_path) | Tests that path to directory returns (False, message) |
| TestCanWriteFile | | Tests the can_write_file function |
| | test_writable_dir(self, temp_path) | Tests that writing to writable directing succeeds |
| | test_restricted_dir(self) | Tests that writing to a restricted directory fails |
| TestPrintNewFile | | Tests the print_new_file function |
| | test_create_write(self, temp_path) | Tests that file is created and contents are written |
| | test_append_file(self, temp_path) | Tests that writing to a file appends new data, not overwritten |
| TestIntegration | | Tests combining multiple functions |
| | test_read_write(self, temp_path) | Tests that reading and writing files can be done in sequence |

### Edge Cases Tested
| Case | Expected Behavior |
| -------- | ------- |
| File not found | Program exits with message: "<file_name> does not exist" |
| Permission denied | Program exits with message: "You do not have permission to read <file_name>" |
| Directory given instead of file | Program exits with message: "<file_name> is not a file" |
| Blank lines in input file | Lines stripped from data, program continues without error |
| More or less than 3 items in a line | Program exits with print out of all data lines with errors. Message: "Reason: list does not contain the expected number of elements" |
| Invalid frequency value | Program exits with print out of all data lines with errors. Message: "Reason: frequency is not an accepted value" |
| Non-numeric dollar amount | Program exits with print out of all data lines with errors. Message: "Reason: dollar amount is not a decimal" |
| Duplicate item names | Program exits with print out of all data lines with errors. Message: "Reason: line item does not have a unique name" |

## Author & Credits
Author: Tiffany M. Mui  
Institution: State University of New York: Empire State University  
Course: CSCI-3025 - Python Programming  
Instructor: Dr. Sahand Ziabari  
Date: 12 Oct 2026  
