# Tiffany M. Mui
# Module 9 Assignment - Data Parser Module
# CSCI-3025: Python Programming
# Purpose: Normalizing and transforming CSVs to pandas dataframes
# Dependencies: TBD


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
    if "Date" in line:
        head_info = None
    else: 
        head_info = line_count
    check = io.dataframe_check(file_name, head_info)
    return check