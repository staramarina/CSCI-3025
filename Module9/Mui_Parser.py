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
        if "date" in line.lower():
            head_info = 0  # Missing column header case
        else:
            head_info = None  # Normal header case
    else:
        head_info = line_count  # Leading rows case
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
    money_re = re.compile(r"^-?\$?[\d,]+(\.\d{1,2})?$")
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
    if 1 == len(date_col_ls):  # Assumes date is always first
        df = df.rename(columns={date_col_ls[0]: "Date"})
    elif 2 == len(date_col_ls):  # Assumes a second date column is post date
        df = df.rename(columns={
            date_col_ls[0]: "Date",
            date_col_ls[1]: "Post Date"
        })
    else:
        return (False, "Could not verify date columns.")
    if 1 == len(mon_col_ls):  # Assumes one money column is amount
        df = df.rename(columns={mon_col_ls[0]: "Amount"})
    elif 2 == len(mon_col_ls):
        if bool(
            ((df[mon_col_ls[0]].notna() & ("" != df[mon_col_ls[0]])) 
             & (df[mon_col_ls[1]].notna() & ("" != df[mon_col_ls[1]]))
            ).any()
        ):  # Assumes amount/balance combo if rows have both values
            df = df.rename(columns={
                mon_col_ls[0]: "Amount",
                mon_col_ls[1]: "Balance"
            })
        else:  # Assumes debit/credit combo if no row has both values
            df = df.rename(columns={
                mon_col_ls[0]: "Debit",
                mon_col_ls[1]: "Credit"
            })
    elif 3 == len(mon_col_ls):  # Assumes Debit/Credit/Balance order
        df = df.rename(columns={
            mon_col_ls[0]: "Debit",
            mon_col_ls[1]: "Credit",
            mon_col_ls[2]: "Balance"
        })
    else:
        return (False, "Could not verify decimal columns.")
    if 0 < len(misc_col_ls):  # Assumes first string column is Description
        df = df.rename(columns={misc_col_ls[0]: "Description"})
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
    if 0 < len(yr_first_match):  # Assumes date first is always YYYY, then MM
        yr_first = True
        day_first = False
        determine = True
        mixed = bool(yr_first_match["sep"].nunique() > 1)
    else:
        yr_first = False
        yr_match = date_col.str.extract(yr_last_re).dropna()
        a = pd.to_numeric(yr_match["x"], errors="coerce")
        b = pd.to_numeric(yr_match["z"], errors="coerce")
        if (12 < a).any() and (12 < b).any():  # Mixed format case
            day_first = False
            determine = False
        elif (12 < a).any():  # Always day first case
            day_first = True
            determine = True
        elif (12 < b).any():  # Always month first case
            day_first = False
            determine = True
        else:  # Ambiguous order case
            day_first = False
            determine = False
        mixed = bool(
            yr_match["sep"].nunique() > 1
            or yr_match["yr"].str.len().nunique() > 1
            or ((12 < a).any() and (12 < b).any())
        )
    return (yr_first, day_first, determine, mixed)


def date_clean(data, col, yr_first, day_first, determine, mixed, err_log):
    """Fixes formatting and converts to datetime within given pandas series
    
    Args:
        data: pandas dataframe that has date column(s)
        col: name of the column that needs cleaning
        yr_first: whether year is first (True/False)
        day_first: whether day is first (True/False)
        determine: whether a determination was made (True/False)
        mixed: whether the column has mixed date formats (True/False)
        err_log: file location to log warnings and errors

    Returns:
        A 2-tuple of the following format:
            [0]: True if clean and conversion successful, otherwise false
            [1]: pandas dataframe on success, otherwise error message
    """
    df = data.copy()
    df[col] = df[col].astype("string").str.strip()
    if determine and not mixed:  # Pass as is case
        df[col] = pd.to_datetime(df[col], errors="coerce", dayfirst=day_first, 
                                 yearfirst=yr_first)
        check = df[col].isna().all()
        if check:
            return (False, f"Dates in '{col}' failed to convert")
        else:
            return (True, df)
    elif determine and mixed:  # Pass as mixed format, pandas should handle
        df[col] = pd.to_datetime(df[col], errors="coerce", dayfirst=day_first, 
                                 yearfirst=yr_first, format="mixed")
        check = df[col].isna().all()
        if check:
            return (False, f"Dates in '{col}' failed to convert")
        else:
            return (True, df)    
    elif not mixed:  # Ambiguous dates, assume month first or abort
        warn_msg = f"Dates in '{col}' are ambiguous, will assume month first"
        force = io.warn_handle(warn_msg, err_log)
        if force:
            df[col] = pd.to_datetime(df[col], errors="coerce")
            check = df[col].isna().all()
            if check:
                return (False, f"Dates in '{col}' failed to convert")
            else:
                return (True, df)
        else:
            return (False, "Process aborted.")
    else:  # Mixed failing case, cannot clean
        return (False, f"Dates in '{col}' have mixed format. "
                "Could not convert.")


def clean_money(data, col):
    """Fixes formatting and converts to number within given pandas series
    
    Args:
        data: pandas dataframe that contains the named money column
        col: name of the column that needs cleaning
    
    Returns:
        A 2-tuple of the following format:
            [0]: True if clean and conversion successful, otherwise false
            [1]: pandas dataframe on success, otherwise error message
    """
    df = data.copy()
    format_clean = (
        df[col].astype("string").str.strip()
        .str.replace(r"^\((.*)\)$", r"-\1", regex=True)
        .str.replace(r"[$,]", "", regex=True))
    df[col] = pd.to_numeric(format_clean, errors="coerce")
    check = df[col].isna().all()
    if check:
        return (False, f"{col} has no values")
    else:
        return (True, df)


def merge_deb_crd(data):
    """Merges the debit and credit columns into single Amount column
    
    Args:
        data: pandas dataframe that has debit and credit columns
    
    Returns:
        A 2-tuple of the following format:
            [0]: True if clean and conversion successful, otherwise false
            [1]: pandas dataframe on success, otherwise error message
    """
    df = data.copy()
    debit = df["Debit"].astype("Float64")
    credit = df["Credit"].astype("Float64")
    conflict = debit.notna() & credit.notna()
    if conflict.any():
        return (False, "Conflicting debit/credit information")
    amount = pd.Series(pd.NA, index=df.index, dtype="Float64")
    amount = amount.fillna(-debit.abs())
    amount = amount.fillna(credit.abs())
    check = amount.isna().all()
    if check:
        return (False, "Failed to merge columns")
    else:
        df["Amount"] = amount
        df = df.drop(columns=["Debit", "Credit"])
        return (True, df)


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
    df = data_raw.copy()

    # Missing headers cleanup
    col_ls = df.columns[df.columns.str.contains("date", case=False)]
    if 0 == len(col_ls):
        warn_msg = "Missing column headers detected, will infer"
        force = io.warn_handle(warn_msg, err_log)
        if force:
            head_check = infer_header(df) # TODO: document this
            if head_check[0]:
                df = head_check[1]
            else:
                return (False, head_check[1])
        else:
            err_msg = "Process aborted."
            return (False, err_msg)

    # Date columns cleanup
    date_col_ls = []
    for col in df.columns:
        if "date" in col.lower():
            date_col_ls.append(col)
    for col in date_col_ls:
        format_check = date_format(df[col])
        clean_check = date_clean(
            df, col, 
            format_check[0], format_check[1], 
            format_check[2], format_check[3],
            err_log
        )
        if not clean_check[0]:
            return (False, clean_check[1])
        elif "post" not in col.lower():
            df = clean_check[1].dropna(subset=[col]) # TODO: document behavior date must be present, but post/posted date does not
            df = df.rename(columns={col: "Date"})
        elif "post" in col.lower():
            df = clean_check[1]
            df = df.rename(columns={col: "Post Date"})
        else:
            df = clean_check[1]

    # Rename and format money columns
    amnt_ls = df.columns[df.columns.str.contains("amount", case=False)]
    if 0 < len(amnt_ls):
        df = df.rename(columns={amnt_ls[0]: "Amount"})
        num_check = clean_money(df, "Amount")
        if num_check[0]:
            df = num_check[1]
        else:
            force = io.warn_handle(num_check[1], err_log)
            if not force:
                return (False, f"Process aborted: {num_check[1]}.")
    bal_ls = df.columns[df.columns.str.contains("bal", case=False)]
    if 0 < len(bal_ls):
        df = df.rename(columns={bal_ls[0]: "Balance"})
        num_check = clean_money(df, "Balance")
        if num_check[0]:
            df = num_check[1]
        else:
            force = io.warn_handle(num_check[1], err_log)
            if not force:
                return (False, f"Process aborted: {num_check[1]}.")
    deb_ls = df.columns[df.columns.str.contains("debit", case=False)]
    if 0 < len(deb_ls):
        df = df.rename(columns={deb_ls[0]: "Debit"})
        num_check = clean_money(df, "Debit")
        if num_check[0]:
            df = num_check[1]
        else:
            force = io.warn_handle(num_check[1], err_log)
            if not force:
                return (False, f"Process aborted: {num_check[1]}.")
    crd_ls = df.columns[df.columns.str.contains("credit", case=False)]
    if 0 < len(crd_ls):
        df = df.rename(columns={crd_ls[0]: "Credit"})
        num_check = clean_money(df, "Credit")
        if num_check[0]:
            df = num_check[1]
        else:
            force = io.warn_handle(num_check[1], err_log)
            if not force:
                return (False, f"Process aborted: {num_check[1]}.")

    # Merge debit and credit columns if they exist
    if ("Debit" in df.columns 
        and "Credit" in df.columns
        and "Amount" not in df.columns):
        merge_check = merge_deb_crd(df)
        if merge_check[0]:
            df = merge_check[1]
        else:
            return (False, merge_check[1])
    elif ("Debit" in df.columns 
        and "Credit" not in df.columns
        and "Amount" not in df.columns):
        df = df.rename(columns={"Debit": "Amount"})
    elif ("Amount" in df.columns):
        return (True, df)
    else:
        return (False, "Indeterminate column labeling.")
