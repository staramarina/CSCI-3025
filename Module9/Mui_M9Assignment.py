# Tiffany M. Mui
# Module 9 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: Personal Expense Tracker
# Dependencies:
#   Standard: sys, copy, datetime, logging, re
#   External: pandas, matplotlib, seaborn
#   Custom: Mui_Ancillary.py, Mui_IO.py,
#           Mui_Parser.py, Mui_Statement.py


import os
import sys
from pathlib import Path
from copy import deepcopy
import matplotlib.pyplot as plt
import Mui_Ancillary as aux
import Mui_IO as io
import Mui_Parser as parse
import Mui_Statement as stmnt


TEST_FILES = {
    'data/bofa_checking_example.csv': True,
    'data/chase_checking_example.csv': True,
    'data/chase_credit_example.csv': True,
    'data/citibank_checking_example.csv': True,
    'data/citibank_credit_example.csv': True,
    'data/sample-bank-transactions.csv': True,
    'data/SCU_checking_example.csv': True,
    'data/SCU_credit_example.csv': True,
    'data/USAA_checking_example.csv': True,
    'data/USAA_credit_example.csv': True,
    'data/wellsfargo_checking_example.csv': True
}


if __name__ == "__main__":
    # Setup
    err_log = "Mui_M9_Log.txt"
    io.log_setup(err_log)
    print("\nWelcome to the expense tracker!\n")

    # Ask user for their transaction files
    file_list = {}
    more_file = "y"
    while more_file in ["Y", "y"]:
        check = io.file_input_handle()
        if check[0]:
            file_list[check[1]] = check[0]  # Forces unique files
            more_file = input("Would you like to include another file (Y/N): ")
        else:
            io.err_handle(check[1], err_log)
            more_file = input("Would you like to try again (Y/N): ")
    if 0 == len(file_list):
        print("No files received. Please restart.")
        sys.exit(1)
    print("File(s) received.")

    # Build dataframes from CSV files
    print("\nBuilding data frame(s).")
    df_list = {}
    for file in file_list:
        check = parse.build_dataframe(file)
        if check[0]:  # If dataframe successfully built
            df_list[file] = check[1]
        else:  # Error creating dataframe
            io.err_handle(check[1], err_log)
            warn_msg = f"Will drop {file}."
            force = io.warn_handle(warn_msg)
            if force:  # Continue with next data set
                print("Continuing with next data set.")
            else:  # Gracefully terminate the program
                io.err_handle("Process aborted.", err_log)
                sys.exit(1)
    if 0 == len(df_list):
        print("No useable files. Please restart.")
        sys.exit(1)
    print("Data frame(s) created.")

    # Parse/clean dataframes
    print("\nParsing and cleaning data.")
    df_clean = {}
    for file, df in df_list.items():
        check = parse.clean_dataframe(df)
        if check[0]:  # If dataframes successfully cleaned
            df_clean[file] = check[1]
        else:  # Error cleaning dataframe
            io.err_handle(check[1], err_log)
            warn_msg = f"Will drop {file} data."
            force = io.warn_handle(warn_msg)
            if force:  # Continue with next data set
                print("Continuing with next data set.")
            else:  # Gracefully terminate the program
                io.err_handle("Process aborted.", err_log)
                sys.exit(1)
    if 0 == len(df_clean):
        print("No useable data. Please restart.")
        sys.exit(1)
    print("Data successfully parsed and cleaned.")

    # Create a list of statement class instances
    print("\nProcessing data.")
    df_class = []
    for file, df in df_clean.items():
        try:
            statement = stmnt.Statement(df, file)
        except TypeError as err:  # error creating statement instance
            warn_msg = f"{err}. Will drop data."
            force = io.warn_handle(warn_msg)
            if force:  # Continue with next data set
                print("Continuing with next data set.")
            else:  # Gracefully terminate the program
                io.err_handle("Process aborted.", err_log)
                sys.exit(1)
        else:
            df_class.append(statement)
    if 0 == len(df_class):
        print("No useable data. Please restart.")
        sys.exit(1)
    print("Data successfully processed.")

    # Add all class instances together into a single class instance
    print("\nCombining data.")
    all_data = deepcopy(df_class[0])
    for statement in df_class[1:]:
        all_data += statement
    print("Data combined.")

    # Check that /charts folder exists and is writable
    probe = os.path.join("charts", ".write_check")
    check = io.can_write_file(probe)
    if check[0]:
        try:
            os.remove(probe)
        except OSError:
            pass
    else:
        io.err_handle(check[1], err_log)
        print("\nPlease check charts directory and restart.")
        sys.exit(1)

    # Map chart functions and file names to menu options
    map_chart = {
        1: (all_data.spend_chart, "charts/spend_chart.png"),
        2: (all_data.cat_chart, "charts/cat_chart.png"),
        3: (all_data.descript_chart, "charts/descript_chart.png"),
        4: (all_data.bal_chart, "charts/bal_chart.png"),
        5: (all_data.top5_chart, "charts/top5_chart.png")
    }

    # Analysis
    print("\n")
    io.print_analysis_menu()
    usr_in = input()
    while 'x' != usr_in:
        select = aux.int_check(usr_in)
        if (select[0]) and (select[1] in map_chart):
            make_chart, file_name = map_chart[select[1]]
            result = make_chart()
            if result[0]:
                save = io.chart_save(result[1], file_name)
                if save[0]:
                    print(save[1])
                else:
                    io.err_handle(save[1], err_log)
                plt.close(result[1][0])
            else:
                print(result[1])
                print("Returning to analysis menu.")
        else:
            print('That doesn\'t seem to be an option.')
        print('')
        io.print_analysis_menu()
        usr_in = input()

    # Closing
    print("\nThank you for using the expense tracker!\n")
