# Tiffany M. Mui
# Module 5 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: Main program for a personal budgeting tool
# Dependencies: MuiIO.py, Mui_M5Calculations.py, TODO see README for full details


from MuiIO import file_exists


if __name__ == "__main__":
    print("Welcome to Tiffany Mui's Budgeting Tool!")
    print("Please enter the file name (with extension) "
          "that contains your income data")
    income_file = input()
    print("Please enter the file name (with extension) "
          "that contains your expense data")
    expense_file = input()
    income_file_check = file_exists(income_file)
    expense_file_check = file_exists(expense_file)
    if income_file_check[0] and expense_file_check[0]:
        print(income_file_check) # test line remove later
        print(expense_file_check) # test line remove later
    elif income_file_check[0]:
        print(f"{income_file_check[1]}, but {expense_file_check[1]}.")
    elif expense_file_check[0]:
        print(f"{expense_file_check[1]}, but {income_file_check[1]}.")
    else:
        print(f"{income_file_check[1]} and {expense_file_check[1]}.")


# Flow Notes:
# perform calculations
# output to user chosen destination

# Other Notes:
# support both single and multiple income sources
# support both single and multiple expenses
# input: need name (string), frequency (string?), dollar amount (float)
# output shows amount and percentage for each expense
# output shows amount and percentage remaining of income after expenses
# need to decide how output is handled