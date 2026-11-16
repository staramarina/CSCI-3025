# Tiffany M. Mui
# Module 8 Assignment - Ancillary Functions Module
# CSCI-3025: Python Programming
# Purpose: General purpose ancillary tools
# Dependencies: datetime


from datetime import datetime


def int_check(num_str): # Copied from Module 6
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
        return (False, f'Invalid input: {err}')


def date_format(date_str): # Heavy reuse from Module 6
    """Formats a string into a datetime
    
    Args:
        date_str: date string input value, expects format YYYY-MM-DD
    
    Returns:
        A 2-tuple with the following format:
            [0]: True if formated as YYYY-MM-DD, otherwise False
            [1]: datetime object if successful, otherwise error message
    """
    if date_str is None:
        return(False, 'Date cannot be none.')
    date_str = str(date_str).strip()
    if 10 != len(date_str):
        return(False, 'Incorrect date length.')
    date_ls = date_str.split('-')
    y_str = date_ls[0]
    m_str = date_ls[1]
    d_str = date_ls[2]
    y_int = int_check(y_str)
    m_int = int_check(m_str)
    d_int = int_check(d_str)
    if y_int[0] and m_int[0] and d_int[0]:
        try:
            date_dtg = datetime(y_int[1], m_int[1], d_int[1])
        except ValueError:
            return (False, 'Not a valid date')
        else:
            return(True, date_dtg)
    else:
        return (False, 'Invalid date formatting')