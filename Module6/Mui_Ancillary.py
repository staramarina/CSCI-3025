# Tiffany M. Mui
# Module 6 Assignment - Ancillary Functions Module
# CSCI-3025: Python Programming
# Purpose: Ancillary functions for the library tool
# Dependencies: datetime


from datetime import datetime, timedelta


def file_exists(file_name): # Note: this was reused from Module 5 Mui_IO.py
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


def int_check(num_str):
    """Determines whether a string can be converted to an integer
    
    Args:
        num_str: an integer as a string

    Returns:
        A 2-tuple in the following format
            [0]: True if string converted to int, otherwise False
            [1]: Integer if successful, otherwise error message
    """
    try:
        num_int = int(num_str)
        return (True, num_int)
    except (ValueError, TypeError) as err:
        return (False, err)


def date_format(date_str):
    """Formats a string into a datetime
        
    Args:
        date_str: a date in string format, expects YYYYMMDD
        
    Returns:
        date_dtg: a date in datetime format if conversion was successful,
            otherwise, None
    """
    max_date = datetime.now()
    min_date = max_date - timedelta(years=100)
    if 8 == len(date_str):
        y_str = date_str[:4]
        m_str = date_str[4:6]
        d_str = date_str[6:]
        y_int = int_check(y_str)
        m_int = int_check(m_str)
        d_int = int_check(d_str)
        if y_int[0] and m_int[0] and d_int[0]:
            if (
                min_date.year <= y_int[1] <= max_date.year
                and 1 <= m_int[1] <= 12
                and 1 <= d_int[1] <= 31
            ):
                try:
                    date_dtg = datetime(y_int[1], m_int[1], d_int[1])
                except ValueError:
                    date_dtg = None
            else:
                date_dtg = None
        else:
            date_dtg = None
    else:
        date_dtg = None
    return date_dtg
