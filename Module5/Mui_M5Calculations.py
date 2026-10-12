# Tiffany M. Mui
# Module 5 Assignment - Budget Tool Calculations Module
# CSCI-3025: Python Programming
# Purpose: Calculations module for a personal budgeting tool
# Dependencies: decimal, copy


from decimal import Decimal, InvalidOperation
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
            removed_data_list[key] = copy.deepcopy(budget[key])
            removed_data_list[key].append("Reason: list does not contain " \
                                          "the expected number of elements")
        elif budget[key][1].lower() not in FREQUENCY_LIST:
            removed_data_list[key] = copy.deepcopy(budget[key])
            removed_data_list[key].append("Reason: frequency is not an " \
                                          "accepted value")
        else:
            try:
                Decimal(budget[key][2])
            except (InvalidOperation, TypeError):
                removed_data_list[key] = copy.deepcopy(budget[key])
                removed_data_list[key].append("Reason: dollar amount is " \
                                              "not a decimal")
    temp_dict = {}
    for key, value in budget.items():
        if value[0] not in temp_dict:
            temp_dict[value[0]] = [key]
        else:
            temp_dict[value[0]].append(key)
    for key, value in temp_dict.items():
        if 1 < len(value):
            for name in value:
                removed_data_list[key] = copy.deepcopy(budget[name])
                removed_data_list[key].append("Reason: line item does " \
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
        budget_formatted[budget_raw[key][0]] = (
            [budget_raw[key][1], 
             budget_raw[key][2]]
             )
    for name in budget_formatted:
        budget_formatted[name][0] = budget_formatted[name][0].lower()
        budget_formatted[name][0] = FREQUENCY_LIST[budget_formatted[name][0]]
        budget_formatted[name][1] = Decimal(budget_formatted[name][1])
    return budget_formatted


def yearly_conversion(budget):
    """Calculates yearly values for income and expenses
    
    Args: 
        budget: a dictionary with list elements containing 
                budgetary data in the following format
            key: name of the item as a string
            [0]: frequency of the transaction per year as an integer
            [1]: dollar amount of the transaction as a decimal
    
    Returns:
        year_budget: a dictionary with list elements containing 
                     budgetary data in the following format
            key: name of the item as a string
            [0]: yearly dollar amount of the transaction as a decimal
    """
    year_budget = {}
    for key in budget:
        year_budget[key] = [Decimal(budget[key][0]) * budget[key][1]]
    return year_budget


def sum_income(income):
    """Calculates total yearly income
    
    Args:
        income: a dictionary with list elements containing 
                income data in the following format
            key: name of the income source as a string
            [0]: income yearly dollar amount in decimal
    
    Returns:
        income_total: total yearly income in decimal
    """
    income_total = Decimal(0)
    for key in income:
        income_total += income[key][0]
    return income_total


def budget_calc(budget, total_income = 1):
    """Calculates monthly income, expenses, and percentages
    
    Args:
        budget: a dictionary with list elements containing 
                income data in the following format
            key: name of the item as a string
            [0]: yearly dollar amount of the transaction as a decimal
        total_income: total yearly income in decimal
    
    Returns:
        monthly_budget: a dictionary with list elements containing 
                      income data in the following format
            key: name of the item as a string
            [0]: monthly dollar amount of the transaction as a decimal
            [1]: percentage of income as a decimal
    """
    monthly_budget = {}
    for key in budget:
        monthly_amount = budget[key][0] / Decimal(12)
        monthly_percent = (budget[key][0] / total_income) * 100
        monthly_budget[key] = [monthly_amount, monthly_percent]
    return monthly_budget


def budget_rounding(budget):
    """Rounds all decimal values for report purposes
    
    Args:
        budget: a dictionary with list elements containing 
                income data in the following format
            key: name of the item as a string
            [0]: monthly dollar amount of the transaction as a decimal
            [1]: percentage of income as a decimal
    
    Returns:
        budget_round: a dictionary with list elements containing 
                      income data in the following format
            key: name of the item as a string (unchanged)
            [0]: monthly dollar amount as a formatted string
            [1]: percentage of income as a formatted string
    """
    budget_round = {}
    for key in budget:
        budget_round[key] = (
            [f"{budget[key][0]:.2f}",
            f"{budget[key][1]:.2f}"]
        )
    return budget_round