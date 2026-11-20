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
        return (True, dtg)
    except (ValueError, TypeError) as err:
        return (False, f"Invalid input: {err}")


def chart_save(chart, file_name, dpi=150):
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
