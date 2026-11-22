# Tiffany M. Mui
# Module 9 Assignment - Data Parser Module
# CSCI-3025: Python Programming
# Purpose: Normalizing and transforming CSVs to pandas dataframes
# Dependencies: TBD


import pandas as pd


def build_dataframe(file_name):
    """Builds a pandas dataframe based on file contents
    
    Args: 
        file_name: file name where the data is stored (assumes CSV)
            Note: assumes it exists
    
    Returns:
        df: pandas dataframe containing the data from the input file
    """
    line_count = 0
    flag = False
    f = open(file_name, "r")
    while not flag:
        line = f.readline()
        if "," in line:
            flag = True
        else:
            line_count += 1
    f.close()
    if 0 == line_count:
        if "Date" in line:
            df = pd.read_csv(file_name)
        else:
            df = pd.read_csv(file_name, header=None)
    else:
        df = pd.read_csv(file_name, header=line_count)
    return df
    # TODO strip any metadata/summary line from the bottom -- do this by verifying date column
    