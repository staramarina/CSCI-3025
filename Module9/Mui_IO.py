# Tiffany M. Mui
# Module 9 Assignment - Input/Output Module
# CSCI-3025: Python Programming
# Purpose: Handles all input/output for the program
# Dependencies: datetime, pandas


from datetime import datetime
import pandas as pd


def file_exists(file_name):  # Duplicated from Module5
    """Checks if a file can be opened and read
    
    Args:
        file_name: name of the file to check, can be absolute or relative path
    
    Returns:
        2-tuple with the following characteristics
        [0]: True if file was successfully opened, otherwise False
        [1]: f-string that provides more information beyond True/False
    """
    try:
        f = open(file_name, 'r')
    except FileNotFoundError: 
        return (False, f'{file_name} does not exist')
    except PermissionError:
        return (False, f'You do not have permission to read {file_name}')
    except IsADirectoryError:
        return (False, f'{file_name} is not a file')
    except OSError as err:
        return (False, f'Failed to read file with error: {err}')
    else:
        f.close()
        return (True, f'{file_name} exists')


def can_write_file(file_name):  # Duplicated from Module5
    """Checks if a file can be appended
    
    Args:
        file_name: name of the file to check, can be absolute or relative path
    
    Returns:
        2-tuple with the following characteristics
        [0]: True if file was successfully opened, otherwise False
        [1]: f-string that provides more information beyond True/False
    """
    try:
        file_open = open(file_name, "a")
    except FileNotFoundError:
        return (False, "Target directory does not exist.")
    except PermissionError:
        return (False, f"You do not have permission to write to {file_name}")
    except OSError as err:
        return (False, f"Failed to write file with error: {err}")
    else:
        file_open.close()
        return (True, f"File printed successfully as {file_name}")


def print_log(data, file_name):  # Duplicated from Module7
    """Prints log entries to an existing file (will create if not present)
    
    Args:
        data: information to be written to the log
        file_name: the file path of the error log
    
    Returns:
        2-tuple with the following characteristics
            [0]: True if file was successfully written, otherwise False
            [1]: f-string that provides more information beyond True/False
    """
    can_write = can_write_file(file_name)
    if can_write[0]:
        time_now = datetime.now()
        with open(file_name, "a") as f:
            f.write(f"{time_now}: {data}\n")
        return can_write
    else:
        return can_write


def dataframe_check(file_name, head_info=0):
    """Checks that data is successfully imported into a pandas dataframe
    
    Args:
        file_name: file name where the data is stored
        head_info: header row location information
    
    Returns:
        2-tuple with the following characteristics
            [0]: True if dataframe was generated, otherwise False
            [1]: pandas dataframe on success, otherwise error message
    """
    try:
        df = pd.read_csv(file_name, header=head_info)
    except FileNotFoundError:
        return (False, f'{file_name} does not exist')
    except pd.errors.EmptyDataError:
        return (False, f'{file_name} has no parsable data.')
    except pd.errors.ParserError as err:
        return (False, f'Encountered parsing error in {file_name}: {err}')
    except ValueError as err:
        return (False, f'Encountered value error {file_name}: {err}')
    else:
        return (True, df)


def chart_save(chart, file_name, dpi=150):  # Duplicated from Module8
    """Saves a chart as an image file

    Args:
        chart: a 2-tuple of (matplotlib figure, matplotlib axes)
        file_name: name of the file to be saved
        dpi: resolution of the saved image in dots/inch

    Returns:
        A 2-tuple with the following format:
            [0]: True if image save was successful, otherwise False
            [1]: f-string providing more information beyond True/False
    """
    fig, ax = chart
    try:
        fig.savefig(file_name, dpi=dpi, bbox_inches="tight")
    except PermissionError:
        return (False, f"You do not have permission to save to {file_name}")
    except (OSError, ValueError) as err:
        return (False, f"Failed to save file with error: {err}")
    else:
        return (True, f"Chart saved to {file_name}")


def file_input_handle():
    """Asks user for file and check for it
    
    Args:
        None
    
    Returns:
        A 2-tuple with the following format:
            [0]: True if file can be read, otherwise False
            [1]: file name if successful, other error message
    """
    usr_in = input("Please enter the file name of your file: ")
    check = file_exists(usr_in)
    if check[0]:
        return (True, usr_in)
    else:
        return (False, check[1])


def err_handle(err_msg, err_log='log.txt'):  # Heavy Reuse from Module7
    """Handles various errors, prints console message and calls print_log
    
    Args:
        err_msg: the error message to log
        err_log: the file path where the log is located
    
    Returns:
        None (console output)
    """
    std_err = 'ERROR: An error has occurred.'
    see_log = f'See {err_log} for details.'
    log_err = 'Could not send error to the logs:'
    flag = print_log(err_msg, err_log)
    if flag[0]:
        print(f'{std_err} {see_log}')
    else:
        print(f'{std_err}')
        print(f'{log_err} {flag[1]}')


def warn_handle(warn_msg, err_log='log.txt'):
    """Handles various warnings, prints console message and calls print_log
    
    Args:
        warn_msg: the warning message to log
        err_log: the file path where the log is located
    
    Returns:
        True to continue, otherwise False
    """
    std_warn = f'WARNING: {warn_msg}. Would you like to proceed (Y/N): '
    log_err = 'Could not send error to the logs:'
    flag = print_log(warn_msg, err_log)
    if not flag[0]:
        print(f'{log_err} {flag[1]}')
    force = input(f'{std_warn}')
    if force in ["Y", "y"]:
        return True
    else:
        return False


def print_analysis_menu():
    """Prints menu with analysis options"""
    print('Please select one of the following options:')
    print('1 -- Overall Spending per Day')
    print('2 -- Spending by Category')
    print('3 -- Spending by Source')
    print('4 -- Overall Balance Changes per Day')
    print('5 -- Top 5 Expenses')
    print('x -- Quit')