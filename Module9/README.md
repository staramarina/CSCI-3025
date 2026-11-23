# Tiffany Mui - Module 9 Assignment

TODO: One-line description

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
- [Testing](#testing)
- [Author/Credits](#author--credits)

---

## Overview
The personal expense tracker was created for State University of New York (SUNY): Empire State University (ESU), CSCI-3025: Python Programming course as the Module 9 assignment.

The personal expense tracker: 
- TODO

Ground work for the following features is included, but not fully implemented:
- TODO

## Features
- TODO

## Installation

### Prerequisites
- Python 3.11 or higher (estimated)
- External Packages
    - pandas - handles data formatting and analysis
    - seaborn - creates graphs
    - matplotlib - handles the underlying settings for graphs

### Setup Steps
1. Download the repository from https://github.com/staramarina/CSCI-3025/tree/main/Module9
2. Verify all files and folders are present
```
TODO
```
3. Install pandas package: (note: it is recommended to utilize a virtual environment to segment dependencies)
```
python -m pip install pandas
```
4. Install seaborn package: (note: this includes matplotlib installation)
```
python -m pip install seaborn
```
5. Ensure Python path includes the Module9 directory or run from within it.

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
    ├── Mui_Ancillary.py                # General purpose ancillary tools
    ├── Mui_IO.py                       # Handles all input/output for the program
    ├── Mui_M9Assignment.py             # Main program
    ├── Mui_Parser.py                   # Normalizing and transforming CSVs to pandas dataframes
    ├── Mui_Statement.py                # Class for bank statements, analysis, and chart generation
    ├── pyproject.toml                  # Project configuration file
    ├── README.md                       # Read me file (current file)
    ├── charts                          # Directory to hold generated charts
    │     └── TODO.png                  # TODO
    ├── tests                           # Test files for unittest
    │     ├── __init__.py               # Tells Python this is a package
    │     ├── test_ancillary.py         # Tests for Mui_Ancillary.py
    │     ├── test_io.py                # Tests for Mui_IO.py
    │     ├── test_parser.py            # Tests for Mui_Parser.py
    │     └── test_statement.py         # Tests for Mui_Statement.py
    └── data                            # Data used for manual tests
          └── TODO.txt                  # TODO
```

## Modules

### Built-in Packages
- TODO

### External Packages - REVIEW
- pandas for handling large data formatting and analysis
    - Estimated Minimum: 2.0
    - Development Environment: 3.1.1
- seaborn for creating graphs
    - Estimated Minimum: 0.13
    - Development Environment: 0.13.2
- matplotlib for handling graph input
    - Estimated Minimum: 3.7
    - Development Environment: 3.11.2

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
- The parser module will attempt to detect the date format with the following rules/assumptions
    - Separating characters are used and include "/" or "-"
    - Dates are not of formats YY-MM-DD, YY/MM/DD, YY-DD-MM, YY/DD/MM, i.e. if the year is first it must be 4 digits followed by month, then day.
    - If the year is last as either YYYY or YY, a check is run to determine whether the day is first or not. In an amiguous case, the assumption is made that month is first (most common in the U.S.) and the user is notified of this assumption. Example: 10/11/12 is interpretted as 11 Oct 2012.
    - Mixed formatting, e.g. MM/DD/YYYY and MM-DD-YY within the same column are handled, but position order must be consistent, i.e. cannot swap between MM/DD/YY and DD/MM/YY. 

## Testing

### Manual Testing
TODO

### Automated Testing
All test cases are compatible with both unittest and pytest.  
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

#### Specfic Module Tests (test_XXX.py)

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
- TODO

### Resources & References
- TODO
