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
//add screenshot

### Sample Output File (budget_data.txt)
//add screenshot

## Project Structure
```
Module5/
    ├── Mui_M5Assignment.py     # Main program (orchestrates workflow)
    ├── MuiIO.py                # I/O module (file handling and verification)
    ├── Mui_M5Calculations.py   # Calculations module (calculations and data verification)
    ├── TestData/               # Example input files
    │   ├── IncomeData.txt      # Example income data
    │   └── ExpenseData.txt     # Example expense data
    └── README.md               # Read me file (current file)
```

## Modules

### Built-in Packages
- decimal.Decimal - Precise financial calculations, avoid floating-point errors
- copy - Copies and deep copies used to prevent unintended mutations of original data

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
//add screenshot

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
