# Tiffany M. Mui
# Module 9 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: Personal Expense Tracker
# Dependencies:
#   Standard: datetime
#   External: pandas, matplotlib, seaborn
#   Custom: Mui_Ancillary.py, Mui_IO.py,
#           Mui_Parser.py, Mui_Statement.py


import Mui_Ancillary as aux
import Mui_IO as io
import Mui_Parser as parse
import Mui_Statement as stmnt


if __name__ == "__main__":
    # Setup
    err_log = "Mui_M9_Log.txt"
    file_list = []

    # Ask user for their transaction files
    more_file = "y"
    while ("Y" or "y") == more_file:
        check = io.csv_input_handle(file_list, err_log)
        if check[0]:
            more_file = input("Would you like to include another file (Y/N): ")
        else:
            more_file = input("Would you like to try again (Y/N): ")

    # Data Parsing -- Actual functions in parse
    # TODO port to pandas dataframe
    # TODO check for rows above header
    # TODO check for header, add if missing
    # TODO detect column names, change to common if needed
    # TODO handle missing data
    # TODO handle data type conversion and malformed data

    # Spin up class instances
    # TODO use cleaned data to generate statement class instances -- init in statement class
    # TODO if more than one instance, combine together -- add method in stmnt

    # Analysis
    # TODO print analysis menu -- call from io
    # TODO check user input with int_check -- call from aux
    # TODO call analysis method -- from stmnt
    # TODO print results
    # TODO ask if user wants another analysis, repeat until N/n

    # Closing
    # TODO program closing message(s)