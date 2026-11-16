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


def float_check(num_str):
    """Determines whether a string can be converted to a float
    
    Args:
        num_str: an floating-point number as a string
    
    Returns:
        A 2-tuple in the following format
            [0]: True if string converted to float, otherwise False
            [1]: Float if successful, otherwise error message
    """
    try:
        num_float = float(num_str)
        return(True, num_float)
    except(ValueError, TypeError) as err:
        return(False, f'Invalid input: {err}')


def dtg_check(date_str, format_str):
    """Determines whether a string can be converted to a datetime object
    
    Args:
        date_str: date string input value
        format_str: format specification of the input value
    
    Returns:
        A 2-tuple with the following format:
            [0]: True if conversion was successful, otherwise False
            [1]: datetime object if successful, otherwise error message
    """
    try:
        dtg = datetime.strptime(date_str, format_str)
        return(True, dtg)
    except(ValueError, TypeError) as err:
        return(False, f'Invalid input: {err}')

def date_format(date_str): # Heavy reuse from Module 6
    """Formats a string into a date
    
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


def dtg_format(date_str):
    """Formats a string into a datetime group
    
    Args:
        date_str: date string input value, expects format YYYY-Mon-DD HH:MM
    
    Returns:
    """
    if date_str is None:
        return(False, 'Date cannot be none.')
    date_str = str(date_str).strip()
    if 17 != len(date_str):
        return(False, 'Incorrect date length')
    date_time = date_str.split(' ')
    date_full = date_time[0].split('-')
    time_full = date_time[1].split(':')
    y_str = date_full[0]
    m_str = date_full[1] # TODO handle this different because Mon, not MM
    d_str = date_full[2]
    hr_str = time_full[0]
    min_str = time_full[1]
    y_int = int_check(y_str)
    m_int = int_check(m_str)
    d_int = int_check(d_str)
    hr_int = int_check(hr_str)
    min_int = int_check(min_str)
    if y_int[0] and m_int[0] and d_int[0] and hr_int[0] and min_int[0]:
        try:
            date_dtg = datetime(y_int[1], m_int[1], d_int[1], 
                                hr_int[1], min_int[1])
        except ValueError:
            return (False, 'Not a valid date')
        else:
            return(True, date_dtg)
    else:
        return (False, 'Invalid date formatting')
    #2026-Nov-01 00:20