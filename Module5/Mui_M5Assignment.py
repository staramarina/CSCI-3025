# Tiffany M. Mui
# Module 5 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: Main program for a personal budgeting tool
# Dependencies: MuiIO.py, Mui_M5Calculations.py, see README for full details
# Provided Example Input Files: 
    # Module5/TestData/IncomeData.txt
    # Module5/TestData/ExpenseData.txt


from MuiIO import file_exists
from MuiIO import print_new_file
import Mui_M5Calculations


if __name__ == "__main__":
    print("Welcome to Tiffany Mui's Budgeting Tool!")
    print("Please enter the file name (with extension) "
          "that contains your income data")
    income_file_name = input()
    print("Please enter the file name (with extension) "
          "that contains your expense data")
    expense_file_name = input()
    income_file_check = file_exists(income_file_name)
    expense_file_check = file_exists(expense_file_name)
    if income_file_check[0] and expense_file_check[0]:
        income = Mui_M5Calculations.generate_budget_object(income_file_name)
        expense = Mui_M5Calculations.generate_budget_object(expense_file_name)
        rm_income = Mui_M5Calculations.check_budget_data(income)
        rm_expense = Mui_M5Calculations.check_budget_data(expense)
        if not rm_income and not rm_expense:
            format_income = Mui_M5Calculations.format_budget_data(income)
            year_income = Mui_M5Calculations.yearly_conversion(format_income)
            total_income = Mui_M5Calculations.sum_income(year_income)
            month_income = Mui_M5Calculations.budget_calc(
                year_income,
                total_income
                )
            round_income = Mui_M5Calculations.budget_rounding(month_income)
            format_expense = Mui_M5Calculations.format_budget_data(expense)
            year_expense = Mui_M5Calculations.yearly_conversion(format_expense)
            month_expense = Mui_M5Calculations.budget_calc(
                year_expense,
                total_income
                )
            round_expense = Mui_M5Calculations.budget_rounding(month_expense)
            report_name = "budget_data.txt"
            print_file = print_new_file(round_income, report_name)
            if print_file[0]:
                print(print_file[1])
                print_file = print_new_file(round_expense, report_name)
            else: 
                print(print_file[1])
        elif not rm_income:
            print("The following lines encountered issues in the expense file")
            print(rm_expense)
        elif not rm_expense: 
            print("The following lines encountered issues in the income file")
            print(rm_income)
        else:
            print("The following lines encountered issues in the income file")
            print(rm_income)
            print("The following lines encountered issues in the expense file")
            print(rm_expense)
    elif income_file_check[0]:
        print(f"{income_file_check[1]}, but {expense_file_check[1]}.")
    elif expense_file_check[0]:
        print(f"{expense_file_check[1]}, but {income_file_check[1]}.")
    else:
        print(f"{income_file_check[1]} and {expense_file_check[1]}.")
