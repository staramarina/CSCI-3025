# Tiffany M. Mui
# Module 7 Assignment - Logging Module
# CSCI-3025: Python Programming
# Purpose: Logging functions for errors
# Dependencies: dateime


from datetime import datetime


def can_write_file(file_name): # duplicated from Module 5 MuiIO.py
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


def print_log(data, file_name):
    """Prints log entries to an existing file (will create if not present)
    
    Args:
        data: information to be written to the log
    
    Returns:
        2-tuple with the following characteristics
        [0]: True if file was successfully written, otherwise False
        [1]: f-string that provides more information beyond True/False
    """
    can_write = can_write_file(file_name)
    if can_write:
        time_now = datetime.now()
        with open(file_name, "a") as f:
            f.write(f"{time_now}: {data}")
        f.close()
        return can_write
    else:
        return can_write