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
- Requests any number of CSV files from the user to be analyzed together.
- Builds pandas dataframes from those CSV files.
- Parses and cleans each dataframe individually to ensure no anomalies result in combining formats.
- Generates statement class instances for each dataframe.
- Combines all statement class instances into a single instance so they can be analyzed together.
  	- File source information is maintained by adding a File Source column in the dataframe.
- An interactive menu is provided to the user for them to select which analysis they would like performed.
- A chart is generated and saved for each requested analysis.
- Once the user is satisfied, they may interactively exit the program.

Ground work for the following features is included, but not fully implemented:
- Mixed date formatting flagging - the case of indeterminate day, month, or year first is caught and the user is prompted with a warning. Other mixed date formatting is caught with format="mixed" to avoid warnings from pandas when supporting unexpected date formats. 
- All files provided are assumed to be analyzed as a single data set, however, this can be changed to support multiple separate or combined data sets with only changes within the main program, since analysis is conducted per class instance. 
- Informational messages are not logged to keep log size relatively small. 

## Features
- Robust error and warning handling with timestamped logging of both.
- Informative warnings print to the console and allows the user to select whether they want to proceed.
- Fairly bank format agnostic file input: only a date column and amount, debit, or credit column is required for basic analysis.
- Multiple analysis options:
  	- Expenses per day over the full data period (available to all data imports that are successfully parsed/cleaned).
  	- Spending by category (requires category data).
  	- Spending by description (requires description data) -- Note: most banks put the source of the expense in the description column, this is not true of all banks.
  	- Maximum balance by day over the full data period (requires balance data).
  	- Top 5 expenses (requires description data) -- Note: if less than 5 expenses are the in the data, the chart can still be generated, it will simply have less slides.

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
```
python Mui_M9Assignment.py
```

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
        ├── sample-bank-transactions.csv      # Sample generic bank export from Utilly (2026)
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

### IO Module (Mui_IO.py)
| Function | Purpose | Return |
| ----- | ------ | ------ |
| file_exists(file_name) | Checks if a file can be opened and read | (True, success message) on success, otherwise (False, error message) |
| can_write_file(file_name) | Checks if a file can be appended | (True, success message) on success, otherwise (False, error message) |
| dataframe_check(file_name, head_info=0) | Checks that data is successfully imported into a pandas dataframe | (True, dataframe) on success, otherwise (False, error message) |
| chart_save(chart, file_name, dpi=150) | Saves a chart as an image file | (True, success message) on success, otherwise (False, error message) |
| file_input_handle() | Asks user for file and check for it | (True, file_name) on success, otherwise (False, error message) |
| log_setup(log_file="log.txt") | Sets up a shared logger to write messages to the given file | common log handler for all logs |
| err_handle(err_msg, err_log='log.txt') | Handles various errors, prints console message and calls logger | None (console/log output) |
| warn_handle(warn_msg, err_log='log.txt') | Handles various warnings, prints console message and calls logger | True to continue, otherwise False |
| print_analysis_menu() | Prints menu with analysis options | None (console output) |

### Parser Module (Mui_Parser.py)
| Function | Purpose | Return |
| ----- | ------ | ------ |
| build_dataframe(file_name) | Builds a pandas dataframe based on file contents | (True, dataframe) on success, otherwise (False, error message) |
| infer_header(data) | Infers header columns if missing from the data set | (True, dataframe) on success, otherwise (False, error message) |
| date_format(column: pd.Series) | Attempts to determine the position of date values in string | A 4-tuple with True/False values for (year first, day first, determination made, mixed date formats) |
| date_clean(data, col, yr_first, day_first, determine, mixed, err_log) | Fixes formatting and converts to datetime within given pandas series | (True, dataframe) on success, otherwise (False, error message) |
| clean_money(data, col) | Fixes formatting and converts to number within given pandas series | (True, dataframe) on success, otherwise (False, error message) |
| merge_deb_crd(data) | "Merges the debit and credit columns into single Amount column | (True, dataframe) on success, otherwise (False, error message) |
| clean_dataframe(data_raw, err_log) | Cleans column naming, missing data, and data type conversions | (True, dataframe) on success, otherwise (False, error message) |

### Statement Module (Mui_Statement.py)
The statement module holds the statement class with the following attributes and methods.

##### Attributes
| Attribute | Purpose | Default Value |
| ----- | ------ | ------ |
| name | name of the data set (typically the file name) | "Transaction Data" |
| df | a pandas dataframe | N/A |

##### Methods
| Method | Purpose | Return |
| ----- | ------ | ------ |
| (@property) df(self) | Used for validated access to statement's dataframe | self.__df |
| _val_df(self, data) | Checks that input data is a pandas dataframe | pandas dataframe on success, otherwise raises TypeError |
| (@df.setter) df(self, data) | Sets the dataframe after validation | validated pandas dataframe |
| __str__(self) | Provides file name and data for a statement as a string | name and data as a string |
| __add__(self, other) | Adds two statement instances together and returns a new combined statement instance | A new combined statement instance |
| spend_analysis(self) | Performs analysis on overall spending per day | A 2-tuple as (True, (dataframe with expense data grouped by date, minimum value, maximum value, daily average)) on success, otherwise (False, error message) |
| spend_chart(self) | Generates the chart for overall spending per day | (True, (matplotlib figure, matplotlib axes)) if data is available, otherwise (False, error message) |
| cat_analysis(self) | Performs analysis on spending by category | (True, dataframe) if Category column exists, otherwise (False, error message) |
| cat_chart(self) | Generates the chart for spending by category | (True, (matplotlib figure, matplotlib axes)) if Category column exists, otherwise (False, error message) |
| descript_analysis(self) | Performs analysis on spending by description | (True, dataframe) if Description column exists, otherwise (False, error message) |
| descript_chart(self) | Generates the chart for spending by description | (True, (matplotlib figure, matplotlib axes)) if Description column exists, otherwise (False, error message) |
| bal_analysis(self) | Performs analysis on maximum balance per day | (True, (dataframe, daily average)) if Balance column exists, otherwise (False, error message) |
| bal_chart(self) | Generates the chart for maximum balance per day | (True, (matplotlib figure, matplotlib axes)) if Balance column exists, otherwise (False, error message) |
| top5_analysis(self) | Performs analysis on top 5 expenses | (True, dataframe) if Description column exists, otherwise (False, error message) |
| top5_chart(self) | Generates the chart for top 5 expenses | (True, (matplotlib figure, matplotlib axes)) if Description column exists, otherwise (False, error message) |

## Data Files
A set of test files is included within the data folder. The examples from USAA and SAFE Credit Union (SCU) were based off real exports and utilize the observed formats, headers, and leading/trailing rows. The examples from Bank of America (BofA), Chase, Citibank, and Wells Fargo were estimated based on information available; as such, the format of the data from these banks may differ from the examples. Checking and savings accounts appeared to share formats, but differed in formatting between checking and credit cards. An example of each was included from the pool of sample banks with the exception of Wells Fargo and BofA credit cards, as there was not enough information available to determine the formatting at a confidence rating of at least 50%. Sample transaction data within these files are based on real, but sanitized, transactions. 

In addition to the generated sample data, a generic "sample-bank-transactions.csv" was obtained from Utilly (2026). This file was also used for testing purposes. 

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
    - There is a minimum of one and a maximum of two date columns. The first being for "Date" or "Transaction Date", the second being for "Posted Date". (Only the first date-like column is used for analysis.)
    - There is a minimum of one and a maximum of three money/float type columns. 
        - If one is present, it is assumed to be "Amount" with mixed positive and negative numbers. 
        - If two are present, a check is run to determine if the combination is "Debit", "Credit" or "Amount", "Balance". If there is any instance of values in both columns .within the row, then the latter is assumed. Otherwise the former is assumed.
        - If three are present, it is assumed to be "Debit", "Credit", and "Balance".
- The parser assumes the following.
    - All rows must have a "Date" value, though "Post Date" may be omitted.
    - Any instance of "bal" represents "Balance", e.g. Running bal., Balance, etc.
    - Any instance of "debit" represents "Debit", e.g. Debit, Amount Debit.
    - Any instance of "credit" represents "Credit", e.g. Credit, Amount Credit.
    - Any instance of "amount" other than those listed above represents "Amount".
    - An "Amount" column must be present.
    - If a column is named "Credit" or "Balance", it is assumed that it must be at least 50% positive values. If this is not true, all values have their signs swapped.
    - Other than the two columns above, it is assumed that all values in the column should be at least 50% negative. If this is not true, all values have their signs swapped. This handles the case where some credit card exports consider expenses to be positive and credits to be negative.
The parser also handles the following.
    - If both "Debit" and "Credit", but not "Amount" are present, "Debit" and "Credit" are merged into a single "Amount" column.
    - If only "Debit" or "Credit" is present, but not "Amount", the column is renamed as "Amount".
    - Fully empty/NA columns are removed.
 
#### Analysis Data Prerequisites
- Overall spending per day can be analyzed with only the minimum data columns, "Date" and "Amount"
- Spending by category requires "Amount" (required through the parser) and "Category" (optional through the parser).
- Spending by Description requires "Amount" (required through the parser) and "Description" (optional through the parser).
- Overall maximum balance per day requires "Amount" (required through the parser) and "Balance" (optional through the parser).
- Top 5 expenses grouping requires "Amount" (required through the parser) and "Description" (optional through the parser).

## Warnings & Errors
- The following are warnings and can be overridden via the console if the user chooses.
    - Ambiguous dates detected, will assume month first if operator selects "Y"/"y", otherwise exit.
    - Missing column header information detected, will infer if operator selects "Y"/"y", otherwise exit.
    - If converting money columns to float data-type fails, the column can be skipped if operator selects "Y"/"y", otherwise exit.
    - If a file could not be converted to a pandas data frame, the operator is given the option to skip that file with "Y"/"y", otherwise exit.
    - If data parsing/cleaning fails on a single pandas data frame, the operator can continue with the next with "Y"/"y", otherwise exit.
- Exceptions to the behavior above are as follows.
  	- An error is generated and displayed to the user when no files were received prior to the user selecting that they have no additional files to input. The program then gracefully exits.
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

1. Insert the following code between the import section and the main section (note: ensure files are present within the data folder).
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
7. Enter the following code between "Add all class instances together into a single class instance" and "Analysis".
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

#### IO Module Tests (test_io.py)
| Class | Method | Purpose |
| ----- | ------ | ------ |
|  | make_chart() | Returns simple matplotlib (figure, axes) for chart_save tests |
| TestFileExists(unittest.TestCase) |  | Tests the file_exists function |
|  | setUp(self) | Setup method to create temporary testing directory |
|  | tearDown(self) | Tear down method to delete temporary testing directory |
|  | test_file_exists_true(self) | "Tests that (True, message) is returned when file exists |
|  | test_file_not_exists(self) | Tests that (False, message) is returned when file does not exist |
|  | test_directory(self) | Tests that path to directory returns (False, message) |
| TestCanWriteFile(unittest.TestCase) |  | Tests the can_write_file function |
|  | setUp(self) | Setup method to create temporary testing directory |
|  | tearDown(self) | Tear down method to delete temporary testing directory |
|  | test_writable_dir(self) | Tests that writing to writable directory succeeds |
|  | test_directory(self) | Tests that path to non-existent directory returns (False, message) |
| TestDataframeCheck(unittest.TestCase) |  | Class to teach dataframe_check(file_name, head_info=0) function |
|  | setUpClass(cls) | Setup method to create temporary testing files for the class |
|  | tearDownClass(cls) | Tear down method to delete temporary testing directory |
|  | setUp(self) | Setup method to create temporary testing directory per method |
|  | test_default_header(self) | Tests the case when there is a header and no leading rows |
|  | test_lead_rows(self) | Tests the case when there is a header and leading rows |
|  | test_no_head(self) | Tests the case when there is no header or leading rows |
|  | test_no_file(self) | Tests the case when the file does not exist |
|  | test_empty_file(self) | Tests the case when the file exists, but it's empty |
|  | test_parse_err(self) | Tests that parsing error is returned if data is malformed |
|  | test_val_err(self) | Tests that a value error is return if invalid header argument received |
| TestChartSave(unittest.TestCase) |  | Class to test chart_save(chart, file_name, dpi=150) function |
|  | setUp(self) | Setup method to create temporary testing directory |
|  | tearDown(self) | Tear down method to delete temporary testing directory |
|  | test_save_success(self) | Tests that a chart was saved successfully |
|  | test_custom_dpi(self) | Tests that a custom dpi is accepted |
|  | test_bad_path(self) | Tests that nonexistent directory returns error |
|  | test_miss_ext(self) | Tests that a file name with missing extension save as .png |
| TestFileInputHandle(unittest.TestCase) |  | Class to test the file_input_handle() function |
|  | setUp(self) | Setup method to create temporary testing directory |
|  | tearDown(self) | Tear down method to delete temporary testing directory |
|  | test_file_there(self) | Tests that (True, message) is returned when file exists |
|  | test_file_not_there(self) | Tests that (False, message) is returned when file does not exist |
| TestLogSetup(unittest.TestCase) |  | Class to test the log_setup(log_file="log.txt") function |
|  | setUp(self) | Setup method to create temporary testing directory and logger |
|  | tearDown(self) | Tear down method to delete testing directory and clear logger |
|  | test_handler(self) | Tests that the handler is attached to the shared logger |
|  | test_duplicate(self) | Tests that calling log_setup twice only results in a single handler |
| TestErrHandle(unittest.TestCase) |  | Class to test the err_handle(err_msg, err_log='log.txt') function |
|  | test_err_log_print(self) | Tests that error logs are printed correctly |
|  | test_err_log_console(self) | Tests the expected error message in the console |
| TestWarnHandle(unittest.TestCase) |  | Class to test the warn_handle(warn_msg, err_log='log.txt') function |
|  | test_warn_log_print(self) | Tests that warning logs are printed correctly |
|  | test_warn_log_console(self) | Tests the expected warning message in the console |
|  | test_force_confirm(self) | Tests the case when user confirms to continue processing |
|  | test_force_deny(self) | Tests the case when user declines to continue process |
|  | test_force_low_confirm(self) | Tests that lower case y works to confirm continuing |
| TestPrinting(unittest.TestCase) |  | Class to test any printing-only functions |
|  | test_analysis_menu(self) | Tests the print_analysis_menu() function |

#### Parser Module Tests (test_parser.py)
| Class | Method | Purpose |
| ----- | ------ | ------ |
| TestBuildDataframe(unittest.TestCase) |  | Class to test the build_dataframe(file_name) function |
|  | setUpClass(cls) | Setup method to create temporary testing files for the class |
|  | tearDownClass(cls) | Tear down method to delete temporary testing directory |
|  | setUp(self) | Setup method to create temporary testing directory per method |
|  | test_default_header(self) | Tests the case when there is a header and no leading rows |
|  | test_lead_rows(self) | Tests the case when there is a header and leading rows |
|  | test_no_head(self) | Tests the case when there is no header or leading rows |
|  | test_empty_file(self) | Tests the case when the file exists, but it's empty |
| TestInferHeader(unittest.TestCase) |  | Class to test the infer_header(data) function |
|  | test_infer_date1(self) | Tests the case of a single date column and one money column |
|  | test_infer_date2(self) | Tests the case of two date columns |
|  | test_infer_date3(self) | Tests the case of three date columns |
|  | test_infer_date0(self) | Tests the case of no date column |
|  | test_infer_deb_crd(self) | Tests the case of two money columns, debit and credit |
|  | test_infer_amt_bal(self) | Tests the case of two money columns, amount and balance |
|  | test_infer_mon3(self) | Tests the case of three money columns |
|  | test_infer_mon0(self) | Tests the case of no money columns |
| TestDateFormat(unittest.TestCase) |  | Class to test the date_format(column: pd.Series) function |
|  | test_year_first(self) | Tests the case when the year is clearly first part |
|  | test_day_first(self) | Tests the case when day is clearly first part |
|  | test_mon_first(self) | Tests the case when day is clearly second part |
|  | test_sep_mixed(self) | Tests the case when there are mixed separators |
|  | test_year_mixed(self) | Tests the case when year is last and mixed YYYY and YY |
|  | test_day_mixed(self) | Tests the case when there is a mix of date first and second |
|  | test_ambiguous(self) | Tests the case when day position cannot be determined |
| TestCleanDate(unittest.TestCase) |  | Class to test the date_clean(data, col, yr_first, day_first, determine, mixed, err_log) function |
|  | setUp(self) | Setup method to create temporary testing directory |
|  | tearDown(self) | Tear down method to delete temporary testing directory |
|  | test_yr1_det(self) | Tests the case when the year is clearly first part |
|  | test_day1_det(self) | Tests the case when day is clearly first part |
|  | test_mon1_det(self) | Tests the case when day is clearly second part |
|  | test_det_sep_mix(self) | Tests the case when there are mixed separators |
|  | test_det_yr_mix(self) | Tests the case when year is last and mixed YYYY and YY |
|  | test_day1_mix(self) | Tests the case when there is a mix of date first and second |
|  | test_all_false_pass(self) | Tests the case when day position cannot be determined |
|  | test_all_false_fail(self) | Tests the case when day position cannot be determined |
|  | test_date_convert_fail(self) | Tests the case when all date values fail to convert |
| TestCleanMoney(unittest.TestCase) |  | Class to test the clean_money(data, col) function |
|  | test_num_convert(self) | Tests that regular numbers are converted to floats |
|  | test_symbol_strip(self) | Tests that additional symbols are stripped when converting |
|  | test_invalid_num(self) | Tests that full invalid numbers result in error message |
|  | test_orig_num(self) | Tests that the original data was not modified |
|  | test_bal_chg(self) | Tests that a mostly negative balance column is updated |
|  | test_amnt_chg(self) | Tests that a mostly positive amount column is updated |
| TestMergeDebCrd(unittest.TestCase) |  | Class to test the merge_deb_crd(data) function |
|  | test_keep_sign(self) | Tests the case of negative debit and positive credit in original |
|  | test_chg_debit(self) | Tests the case when debit is positive |
|  | test_chg_credt(self) | Tests the case when credit is negative |
|  | test_deb_crd_conflict(self) | Tests the case when there is data in both debit and credit columns |
|  | test_deb_crd_null(self) | Tests the case when neither debit nor credit have data |
|  | test_deb_crd_orig(self) | Tests that the original dataframe still has debit/credit columns |
| TestCleanDataframe(unittest.TestCase) |  | Class to test the clean_dataframe(data_raw, err_log) function |
|  | setUp(self) | Setup method to create temporary testing directory |
|  | tearDown(self) | Tear down method to delete temporary testing directory |
|  | test_simple_clean_success(self) | Tests that case of Date, Amount, Description, Balance passes |
|  | test_call_infer_header(self) | Tests that the infer_header is called appropriately when forced |
|  | test_header_warn_abort(self) | Tests that aborting at the header warning stops processing |
|  | test_multi_date(self) | Tests the case of multiple dates in header rows |
|  | test_force_ambig_date(self) | Tests when ambiguous date assumption is accepted |
|  | test_abort_ambig_date(self) | Tests when ambiguous date processing is aborted |
|  | test_force_bad_num(self) | Tests when number conversion failure is accepted |
|  | test_abort_bad_num(self) | Tests when number conversion failure is aborted |
|  | test_deb_crd_merge(self) | Tests that debit/credit columns renamed and merged |
|  | test_deb_crd_conflict(self) | Tests that debit/credit merge conflicts are integrated |
|  | test_debit_only(self) | Tests the case where debit is the only money column |
|  | test_credit_only(self) | Tests the case where credit is the only money column |
|  | test_column_conflict(self) | Tests the case when column labeling is conflicting |
|  | test_no_date_col(self) | Tests the case where no date column exists |
|  | test_no_money_col(self) | Tests the case where no amount, debit, or credit column exists |

#### Statement Class Module Tests (test_statement.py)
| Class | Method | Purpose |
| ----- | ------ | ------ |
| StmntBuild |  | Class to build various statement class instances for test cases |
|  | build_lrg(self) | Builds and returns a larger pandas dataframe for analysis/charts |
|  | build_df6(self) | Builds and returns a pandas dataframe with 6 columns |
|  | build_df4(self) | Builds and returns a pandas dataframe with 4 columns |
|  | build_min(self) | Builds and returns a pandas dataframe with only Date and Amount |
|  | build_default_stmnt(self) | Builds a default statement instance |
|  | build_df6_stmnt(self) | Builds a statement instance using the 6 column dataframe |
|  | build_df4_stmnt(self) | Builds a statement instance using the 4 column dataframe |
|  | build_any_stmnt(self, df, name) | Returns a statement instance with specified input |
| TestStmntMagic(StmntBuild, unittest.TestCase) |  | Class to test the magic functions in the statement class |
|  | setUp(self) | Setup method to create test statement class instances |
|  | test_default_init(self) | Tests the case when name is not supplied on initialization |
|  | test_name_override(self) | Tests that the name is overridden when specified on initialization |
|  | test_df_pass(self) | Tests that a dataframe is successfully added to class instance |
|  | test_not_dataframe(self) | Tests the case when the data variable is not a dataframe on initialization |
|  | test_string_method(self) | Tests that the __str__ method returns name and data |
|  | test_add_method(self) | Tests that the __add__ method returns a new combined instance |
| TestSpendAnalysis(StmntBuild, unittest.TestCase) |  | Class to test the spend_analysis() method |
|  | setUp(self) | Setup method to create test statement class instances |
|  | test_spend_income(self) | Tests that income is excluded from expenses |
|  | test_spend_pad(self) | Tests that missing dates are added |
|  | test_spend_stats(self) | Tests than min, max, and avg values are calculated correctly |
|  | test_spend_orig(self) | Tests that the original dataframe is unmodified |
| TestSpendChart(StmntBuild, unittest.TestCase) |  | Class to test the spend_chart() method |
|  | setUp(self) | Setup method to create test statement class instances |
|  | tearDown(self) | Closes charts after each test |
|  | test_spend_fig(self) | Tests that both figure and axes is returned |
|  | test_spend_label(self) | Tests that the chart title and axis label are correct |
|  | test_spend_legend(self) | Tests that all legend items are present |
| TestCatAnalysis(StmntBuild, unittest.TestCase) |  | Class to test the cat_analysis() method |
|  | setUp(self) | Setup method to create test statement class instances |
|  | test_cat_income(self) | Tests that income is excluded from expenses |
|  | test_cat_agg(self) | Tests that amount values are aggregated |
|  | test_cat_sort(self) | Tests that categories are sorted by amount |
|  | test_cat_err(self) | Tests the case when there is no Category column |
|  | test_cat_orig(self) | Tests that the original dataframe is unmodified |
| TestCatChart(StmntBuild, unittest.TestCase) |  | Class to test the cat_chart() method |
|  | setUp(self) | Setup method to create test statement class instances |
|  | tearDown(self) | Closes charts after each test |
|  | test_cat_fig(self) | Tests that both figure and axes is returned |
|  | test_cat_label(self) | Tests that the chart title and axis label are correct |
|  | test_cat_chart_err(self) | Tests the case when Category is not a column |
| TestDescriptAnalysis(StmntBuild, unittest.TestCase) |  | Class to test the descript_analysis() method |
|  | setUp(self) | Setup method to create test statement class instances |
|  | test_descript_income(self) | Tests that income is excluded from expenses |
|  | test_descript_sort(self) | Tests that descriptions are sorted by amount |
|  | test_descript_err(self) | Tests the case when there is no Description column |
|  | test_descript_orig(self) | Tests that the original dataframe is unmodifed |
| TestDescriptChart(StmntBuild, unittest.TestCase) |  | Class to test the descript_chart() method |
|  | setUp(self) | Setup method to create test statement class instances |
|  | tearDown(self) | Closes charts after each test |
|  | test_descript_fig(self) | Tests that both figure and axes is returned |
|  | test_descript_label(self) | Tests that the chart title and axis label are correct |
|  | test_descript_chart_err(self) | Tests the case when Description is not a column |
| TestBalAnalysis(StmntBuild, unittest.TestCase) |  | Class to test the bal_analysis() method |
|  | setUp(self) | Setup method to create test statement class instances |
|  | test_bal_max(self) | Tests that balance values only reflect maximum |
|  | test_bal_stats(self) | Tests than avg value is calculated correctly |
|  | test_bal_err(self) | Tests the case when there is no Balance column |
|  | test_bal_orig(self) | Tests that the original dataframe is unmodified |
| TestBalChart(StmntBuild, unittest.TestCase) |  | Class to test the bal_chart() method |
|  | setUp(self) | Setup method to create test statement class instances |
|  | tearDown(self) | Closes charts after each test |
|  | test_bal_fig(self) | Tests that both figure and axes is returned |
|  | test_bal_label(self) | Tests that the chart title and axis label are correct |
|  | test_bal_legend(self) | Tests that all legend items are present |
|  | test_bal_chart_err(self) | Tests the case when Balance is not a column |
| TestTopAnalysis(StmntBuild, unittest.TestCase) |  | Class to test the top5_analysis() method |
|  | setUp(self) | Setup method to create test statement class instances |
|  | test_top_income(self) | Tests that income is excluded from expenses |
|  | test_top_sort(self) | Tests that descriptions are sorted by amount |
|  | test_top_less(self) | Tests the case when there are less than five descriptions |
|  | test_top_more(self) | Tests the case when there are more than five descriptions |
|  | test_top_err(self) | Tests the case when there is no Description column |
|  | test_top_orig(self) | Tests that the original dataframe is unmodifed |
| TestTopChart(StmntBuild, unittest.TestCase) |  | Class to test the top5_chart() method |
|  | setUp(self) | Setup method to create test statement class instances |
|  | tearDown(self) | Closes charts after each test |
|  | test_top_fig(self) | Tests that both figure and axes is returned |
|  | test_top_label(self) | Tests that the chart title is correct |
|  | test_top_less_chart(self) | Tests that less than 5 wedges are included |
|  | test_top_more_chart(self) | Tests that 6 wedges are included |
|  | test_top_chart_err(self) | Tests the case when Description is not a column |

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
