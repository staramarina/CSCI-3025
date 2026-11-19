# Tiffany M. Mui
# Module 8 Assignment - Ancillary Functions Module
# CSCI-3025: Python Programming
# Purpose: General purpose ancillary tools
# Dependencies: datetime


from datetime import datetime


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


# TODO: function to display chart