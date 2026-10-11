# Tiffany M. Mui
# Module 5 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: Main program for a personal budgeting tool
# Dependencies: MuiIO.py, Mui_M5Calculations.py, TODO see README for full details


from MuiIO import file_exists


# TODO build the program
if __name__ == "__main__":
    print("Welcome to Tiffany Mui's Budgeting Tool!")
    print("Please enter the file name (with extension) "
          "that contains your income data")
    file_name = input()
    file_check = file_exists(file_name)
    print(file_check)

# Flow Notes:
# open with a menu, ask for choice between file and console input
# if file input, ask for path/filename for income and expenses
# if console input, ask for user input for each item, check if input is done
# ask if user wants file or console output
# perform calculations
# output to user chosen destination

# Other Notes:
# support both single and multiple income sources
# support both single and multiple expenses
# input: need name (string), frequency (string?), dollar amount (float)
# output shows amount and percentage for each expense
# output shows amount and percentage remaining of income after expenses
# need to decide how output is handled