# Tiffany M. Mui
# Module 5 Assignment - Budget Tool Calculations Module
# CSCI-3025: Python Programming
# Purpose: Calculations module for a personal budgeting tool


from decimal import Decimal
import copy


FREQUENCY_LIST = {
    "yearly": 1,
    "semiannually": 2,
    "quarterly": 4,
    "monthly": 12,
    "bimonthly": 24,
    "weekly": 52.143,
    "daily": 365.2425,
}



def generate_budget_object(file_name):
    """Generates a budget object, can be used for income and expenses
    
    Args:
        file_name: name of the file that contains the data

    Returns:
        budget: a dictionary containing a list of input data for each file line
    """
    budget = {}
    count = 0
    reader = open(file_name)
    for line in reader:
        if line.isspace():
            continue
        else:
            line = line.strip()
            data = line.split(", ")
            budget[count] = data
            count += 1
    reader.close()
    return budget


def check_budget_data(budget):
    """Checks that the amount and type of data is correct
    
    Args:
        budget: a dictionary with elements as a list containing budgetary data
            The following list elements are expected
            [0]: unique name of the item as a string
            [1]: frequency of the transaction as a string
            [2]: dollar amount of the transaction as a decimal
    
    Returns:
        removed_data_list: list of key, value pairs that were removed
    """
    removed_data_list = {}
    for key in budget:
        if 3 != len(budget[key]):
            new_key = copy.copy(key)
            removed_data_list[new_key] = copy.deepcopy(budget[key])
            removed_data_list[new_key].append("Reason: list does not contain " \
                                          "the expected number of elements")
        elif budget[key][1] not in FREQUENCY_LIST:
            new_key = copy.copy(key)
            removed_data_list[new_key] = copy.deepcopy(budget[key])
            removed_data_list[new_key].append("Reason: frequency is not an " \
                                          "accepted value")
        else:
            try:
                Decimal(budget[key][2])
            except (ValueError, TypeError):
                new_key = copy.copy(key)
                removed_data_list[new_key] = copy.deepcopy(budget[key])
                removed_data_list[new_key].append("Reason: dollar amount is " \
                                              "not a decimal")
    for key_outer in budget:
        for key_inner in budget:
            if budget[key_inner][0] == budget[key_outer][0]:
                new_key = copy.copy(key)
                removed_data_list[new_key] = copy.deepcopy(budget[key])
                removed_data_list[new_key].append("Reason: line item does " \
                                                  "not have a unique name")
    return removed_data_list


def format_budget_data(budget_raw):
    """Prepares budgetary data for calculations
    
    Args:
        budget_raw: a dictionary with list elements containing budgetary data
            The following list elements are expected
            [0]: unique name of the item as a string
            [1]: frequency of the transaction as a string
            [2]: dollar amount of the transaction as a decimal in string form
    
    Returns:
        budget_formatted: a dictionary with list elements containing 
                         budgetary data in the following format
            key: name of the item as a string
            [0]: frequency of the transaction per year as an integer
            [1]: dollar amount of the transaction as a decimal
    """
    budget_formatted = {}
    for key in budget_raw:
        budget_formatted[budget_raw[key][0]] = [budget_raw[key][1], budget_raw[key][2]]
    for name in budget_formatted:
        budget_formatted[name][0] = FREQUENCY_LIST[budget_formatted[name][0]]
        budget_formatted[name][1] = Decimal(budget_formatted[name][1])
    return budget_formatted

# TODO calculate percentage of income used for each expense

# TODO calcluate remaining income and percentage