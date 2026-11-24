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


def infer_header(data):
    """Infers header columns if missing from the data set
    
    Args: pandas dataframe with placeholder column names
    
    Returns:
        A 2-tuple of the following format:
            [0]: True if headers were added, otherwise false
            [1]: pandas dataframe on success, otherwise error message
    """
    df = data.copy()
    yr_first_re = re.compile(
        r"^(?P<yr>\d{4})(?P<sep>[-/])(?P<x>\d{1,2})(?P=sep)(?P<z>\d{1,2})$"
    )
    yr_last_re = re.compile(
        r"^(?P<x>\d{1,2})(?P<sep>[-/])(?P<z>\d{1,2})(?P=sep)(?P<yr>\d{1,2}|\d{4})$"
    )
    money_re = re.compile(r"^-?\$?[\d,]+(\.\d{1,2})$")
    date_col_ls = []
    mon_col_ls = []
    misc_col_ls = []
    for col in df.columns:
        df[col] = df[col].astype("string").str.strip()
        if (
            df[col].str.match(yr_first_re).any()
            or df[col].str.match(yr_last_re).any()
        ):
            date_col_ls.append(col)
        elif df[col].str.match(money_re).any():
            mon_col_ls.append(col)
        else:
            misc_col_ls.append(col)
    if 1 == len(date_col_ls):
        df.rename(columns={date_col_ls[0]: "Date"}, inplace=True)
    elif 2 == len(date_col_ls):
        df.rename(columns={
            date_col_ls[0]: "Date",
            date_col_ls[1]: "Post Date"
        }, inplace=True)
    else:
        return (False, "Could not verify date columns.")
    if 1 == len(mon_col_ls):
        df.rename(columns={mon_col_ls[0]: "Amount"}, inplace=True)
    elif 2 == len(mon_col_ls):
        if bool(
            ((df[mon_col_ls[0]].notna() & ("" != df[mon_col_ls[0]])) 
             & (df[mon_col_ls[1]].notna() & ("" != df[mon_col_ls[1]]))
            ).any()
        ):
            df.rename(columns={
                mon_col_ls[0]: "Amount",
                mon_col_ls[1]: "Balance"
            }, inplace=True)
        else:
            df.rename(columns={
                mon_col_ls[0]: "Debit",
                mon_col_ls[1]: "Credit"
            }, inplace=True)
    elif 3 == len(mon_col_ls):
        df.rename(columns={
            mon_col_ls[0]: "Debit",
            mon_col_ls[1]: "Credit",
            mon_col_ls[2]: "Balance"
        }, inplace=True)
    else:
        return (False, "Could not verify decimal columns.")
    if 0 < len(misc_col_ls):
        df.rename(columns={misc_col_ls[0]: "Description"}, inplace=True)
    return (True, df)


def date_format(column: pd.Series):
    """Attempts to determine the position of date values in string
    
    Args:
        column: a pandas series with date values as strings
    
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


def date_clean(data, col, yr_first, day_first, determine, mixed):
    """Fixes formatting and converts to datetime of given pandas series
    
    Args:
        data: pandas dataframe that has date column(s)
        col: name of the column that needs cleaning
        yr_first: whether year is first (True/False)
        day_first: whether day is first (True/False)
        determine: whether a determination was made (True/False)
        mixed: whether the column has mixed date formats (True/False)

    Returns:
        A 2-tuple of the following format:
            [0]: True if clean and conversion successful, otherwise false
            [1]: pandas dataframe on success, otherwise error message
    """
    df = data.copy()
    df[col] = df[col].astype("string").str.strip()
    if determine and not mixed:
        df[col] = pd.to_datetime(df[col], errors="coerce", dayfirst=day_first, 
                                 yearfirst=yr_first)
        check = df[col].isna().all()
        if check:
            return (False, f"Dates in '{col}' failed to convert")
        else:
            return (True, df)
    elif determine and mixed:
        df[col] = pd.to_datetime(df[col], errors="coerce", dayfirst=day_first, 
                                 yearfirst=yr_first, format="mixed")
        check = df[col].isna().all()
        if check:
            return (False, f"Dates in '{col}' failed to convert")
        else:
            return (True, df)    
    elif not mixed:
        return (False, f"Dates in '{col}' are ambiguous, "
                "verify month first assumption")
    else:
        return (False, f"Dates in '{col}' have mixed format. "
                "Could not convert.")


def clean_dataframe(data_raw, err_log):
    """Cleans column naming, missing data, and data type conversions
    
    Args:
        data_raw: full raw data pulled from the source, leading rows trimmed
        err_log: file location to log warnings and errors
    
    Returns:
        A 2-tuple of the following format:
            [0]: True if clean and conversion successful, otherwise false
            [1]: pandas dataframe on success, otherwise error message
    """
    data_clean = data_raw.copy()
    col_ls = data_clean[data_clean.columns.str.contains("date", case=False)]
    if 0 == len(col_ls):
        warn_msg = "Missing column headers detected, will infer"
        force = io.warn_handle(warn_msg, err_log)
        if force:
            head_check = infer_header(data_clean) # TODO: document this
            if head_check[0]:
                data_clean = head_check[1]
            else:
                return (False, head_check[1])
        else:
            err_msg = "Process aborted."
            return (False, err_msg)
    date_col_ls = []
    for col in data_clean.columns:
        if "date" in col.lower():
            date_col_ls.append(col)
    for col in date_col_ls:
        format_check = date_format(data_clean[col])
        clean_check = date_clean(
            data_clean, col, 
            format_check[0], format_check[1], 
            format_check[2], format_check[3]
        )
        if not clean_check[0]:
            return (False, clean_check[1]) # TODO: document this, be sure to raise as needed in main
        elif "post" not in col.lower():
            data_clean = clean_check[1].dropna(subset=[col]) # TODO: document behavior date must be present, but post/posted date does not
            data_clean.rename(columns={col: "Date"}, inplace=True)
        elif "post" in col.lower():
            data_clean = clean_check[1]
            data_clean.rename(columns={col: "Post Date"}, inplace=True)
        else:
            data_clean = clean_check[1]
    bal_ls = data_clean[data_clean.columns.str.contains("bal", case=False)]
    if 0 < len(bal_ls):
        data_clean.rename(columns={bal_ls[0]: "Balance"}, inplace=True)
    chk_ls = data_clean[data_clean.columns.str.contains("check", case=False)]
    if 0 < len(chk_ls):
        data_clean.rename(columns={chk_ls[0]: "Check Number"}, inplace=True)
    deb_ls = data_clean[data_clean.columns.str.contains("debit", case=False)]
    if 0 < len(deb_ls):
        data_clean.rename(columns={deb_ls[0]: "Debit"}, inplace=True)
    cdt_ls = data_clean[data_clean.columns.str.contains("credit", case=False)]
    if 0 < len(cdt_ls):
        data_clean.rename(columns={cdt_ls[0]: "Credit"}, inplace=True)
    amnt_ls = data_clean[data_clean.columns.str.contains("amount", case=False)]
    if 0 < len(amnt_ls):
        data_clean.rename(columns={amnt_ls[0]: "Amount"}, inplace=True)
            

    # TODO: merge debit and credit into amount
    # TODO: convert amount to number, fix signs as needed (expense should  be negative)


