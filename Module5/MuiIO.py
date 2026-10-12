# Tiffany M. Mui
# Module 5 Assignment - I/O Module
# CSCI-3025: Python Programming
# Purpose: Input/Output module for handling files and console


def file_exists(file_name):
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


def can_write_file(file_name):
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


def print_new_file(data_dict, file_name):
    """Prints a dictionary to an existing file (will create if not present)
    
    Args:
        data_dict: a dictionary with iterable elements (e.g. list)
    
    Returns:
        2-tuple with the following characteristics
        [0]: True if file was successfully written, otherwise False
        [1]: f-string that provides more information beyond True/False
    """
    can_write = can_write_file(file_name)
    if can_write:
        with open(file_name, "a") as f:
            for key, value in data_dict.items():
                f.write(f"{key}")
                for i in range(len(value)):
                    f.write(f", {value[i]}")
                f.write("\n")
        f.close()
        return can_write
    else:
        return can_write