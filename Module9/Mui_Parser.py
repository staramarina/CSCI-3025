# Tiffany M. Mui
# Module 9 Assignment - Data Parser Module
# CSCI-3025: Python Programming
# Purpose: Normalizing and transforming CSVs to pandas dataframes
# Dependencies: TBD


import re
import pandas as pd
import Mui_IO as io


def build_dataframe(file_name):
    """Builds a pandas dataframe based on file contents
    
    Args: 
        file_name: file name where the data is stored (assumes CSV)
            Note: assumes it exists
    
    Returns:
        check: 2-tuple with the following characteristics
            [0]: True if dataframe was generated, otherwise False
            [1]: pandas dataframe on success, otherwise error message
    """
    line_count = 0
    line = ''
    with open(file_name, "r") as f: 
        for line in f:
            if line.isspace():
                continue
            elif "," in line:
                char_count = line.count(",")
                if 3 > char_count:
                    line_count += 1
                    continue
                else:
                    break
            else:
                line_count += 1
                continue
    if 0 == line_count:
        if "Date" in line:
            head_info = 0
        else:
            head_info = None
    else:
        head_info = line_count
    check = io.dataframe_check(file_name, head_info)
    return check


def date_format(column: pd.Series):
    """Attempts to determine the position of date values in string
    
    Args:
        date_str: a date as a string with year, month, and day values
    
    Returns:
        date_pos: A 4-tuple of the following format
            [0]: whether year is first (True/False)
            [1]: whether day is first (True/False)
            [2]: whether a determination was made (True/False)
            [3]: whether the column has mixed date formats (True/False)
    """
    date_col = column.astype("string").str.strip()
    date_col = date_col.dropna()
    date_col = date_col[date_col != ""]
    yr_first_re = re.compile(
        r"^(?P<yr>\d{4})(?P<sep>[-/])(?P<x>\d{1,2})(?P=sep)(?P<z>\d{1,2})$"
    )
    yr_last_re = re.compile(
        r"^(?P<x>\d{1,2})(?P<sep>[-/])(?P<z>\d{1,2})(?P=sep)(?P<yr>\d{1,2}|\d{4})$"
    )
    yr_first_match = date_col.str.extract(yr_first_re).dropna()
    if 0 < len(yr_first_match):
        yr_first = True
        day_first = False
        determine = True
        mixed = bool(yr_first_match["sep"].nunique() > 1)
    else:
        yr_first = False
        yr_match = date_col.str.extract(yr_last_re).dropna()
        a = pd.to_numeric(yr_match["x"], errors="coerce")
        b = pd.to_numeric(yr_match["z"], errors="coerce")
        if (12 < a).any() and (12 < b).any():
            day_first = False
            determine = False
        elif (12 < a).any():
            day_first = True
            determine = True
        elif (12 < b).any():
            day_first = False
            determine = True
        else:
            day_first = False
            determine = False
        mixed = bool(
            yr_match["sep"].nunique() > 1
            or yr_match["yr"].str.len().nunique() > 1
            or ((12 < a).any() and (12 < b).any())
        )
    return (yr_first, day_first, determine, mixed)


def clean_dataframe(data_raw):
    """Cleans column naming, missing data, and data type conversions
    
    Args:
        data_raw: full raw data pulled from the source, leading rows trimmed
    
    Returns:
        data_clean: data with standardized column names and correct data types
    """
    # TODO handle case of missing column names
    data_clean = data_raw.copy()
    date_col_ls = []
    for col in data_clean.columns:
        if "date" in col.lower():
            date_col_ls.append(col)
    for col in date_col_ls:
        if "post" not in col.lower():
            data_clean.rename(columns={col: "Date"}, inplace=True,)
            format_check = date_format(data_clean["Date"])
            # TODO handle mixed format, formats in files: MM/DD/YYYY, MM/DD/YY, MM-DD-YY
            # TODO handle determine = False, mixed = True case (ambiguous and mixed)
            # TODO change to datetime


    # TODO detect column names, change to common if needed
    # TODO handle missing data
    # TODO handle data type conversion and malformed data, strip any metadata/summary line from the bottom