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
