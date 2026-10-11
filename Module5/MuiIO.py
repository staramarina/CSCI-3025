# Tiffany M. Mui
# Module 5 Assignment
# CSCI-3025: Python Programming
# Purpose: Input/Output module for handling files and console input


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