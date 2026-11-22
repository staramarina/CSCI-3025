# Tiffany M. Mui
# Module 9 Assignment - Ancillary Functions Module
# CSCI-3025: Python Programming
# Purpose: General purpose ancillary tools
# Dependencies: None


def int_check(num_str):  # Duplicated from Module6
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
