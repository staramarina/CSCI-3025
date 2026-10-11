# Tiffany M. Mui
# Module 5 Assignment - Budget Tool Calculations Module
# CSCI-3025: Python Programming
# Purpose: Calculations module for a personal budgeting tool


def generate_budget_object(file_name):
    """Generates a budget object, can be used for income and expenses
    
    Args:
        file_name: name of the file that contains the data

    Returns:
        budget: a dictionary containing a list of input data for each file line
        --move below to later for the data checks
        [0]: name of the item as a string
        [1]: frequency of the transaction --need to decide how this behaves
        [2]: dollar amount of the transaction as a float
    """
    budget = {}
    count = 0
    reader = open(file_name)
    for line in reader:
        data = line.split(", ")
        if 0 == len(data): 
            continue
        else: 
            budget[count] = data
            count += 1
    reader.close()
    return budget

# TODO data check on dict
    # correct amount of data
        # handle correct, less, and more data cases
    # correct data types
        # check frequency and dollar amount

# TODO calculate percentage of income used for each expense

# TODO calcluate remaining income and percentage