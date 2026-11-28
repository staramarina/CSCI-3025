# Tiffany M. Mui
# Module 9 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: Personal Expense Tracker
# Dependencies:
#   Standard: sys, copy, datetime, logging, re
#   External: pandas, matplotlib, seaborn
#   Custom: Mui_Ancillary.py, Mui_IO.py,
#           Mui_Parser.py, Mui_Statement.py


import sys
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

USAA_CHECK = 'priv_test/checking2_scrubbed.csv' # good description and category
USAA_CREDIT = 'priv_test/credit2_scrubbed.csv'  # good to combo with checking2
SAFE_CREDIT = 'priv_test/credit1_scrubbed.csv' # good balance, don't use description

REAL_FILES = {
    #USAA_CHECK: True,
    USAA_CREDIT: True,
    SAFE_CREDIT: True
}


if __name__ == "__main__":
    # Setup
    err_log = "Mui_M9_Log.txt"
    io.log_setup(err_log)
    print("\nWelcome to the expense tracker!\n")

    # Ask user for their transaction files
    """ # TODO add this back in later when ready to conduct full testing.
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
    """
    print("File(s) received.")

    # Build dataframes from CSV files
    print("\nBuilding data frame(s).")
    df_list = {}
    for file in REAL_FILES:  # TODO replace with file_list later
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
            warn_msg = f"Will drop data."
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
            force = io.warn_handle(err)
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

    # Analysis
    print("\n")
    io.print_analysis_menu()
    usr_in = input()
    while 'x' != usr_in:
        select = aux.int_check(usr_in)
        match select[1]:
            case 1:  # Overall Spending per Day
                spend = all_data.spend_chart()
                if spend[0]:
                    check_spend = io.chart_save(spend[1], 
                                                "charts/spend_chart.png")
                    if check_spend[0]:
                        print(check_spend[1])
                        plt.close(check_spend[1][0])
                    else:
                        io.err_handle(check_spend[1], err_log)
                else:
                    force = io.warn_handle(spend[1])
                    if force:
                        print("Returning to analysis menu.")
                    else:
                        io.err_handle("Process aborted.", err_log)
                        sys.exit(1)
            case 2:  # Spending by Category
                cat = all_data.cat_chart()
                if cat[0]:
                    check_cat = io.chart_save(cat[1], 
                                                "charts/cat_chart.png")
                    if check_cat[0]:
                        print(check_cat[1])
                        plt.close(check_cat[1][0])
                    else:
                        io.err_handle(check_cat[1], err_log)
                else:
                    force = io.warn_handle(cat[1])
                    if force:
                        print("Returning to analysis menu.")
                    else:
                        io.err_handle("Process aborted.", err_log)
                        sys.exit(1)
            case 3:  # Spending by Description
                des = all_data.descript_chart()
                if des[0]:
                    check_des = io.chart_save(des[1], 
                                                "charts/descript_chart.png")
                    if check_des[0]:
                        print(check_des[1])
                        plt.close(check_des[1][0])
                    else:
                        io.err_handle(check_des[1], err_log)
                else:
                    force = io.warn_handle(des[1])
                    if force:
                        print("Returning to analysis menu.")
                    else:
                        io.err_handle("Process aborted.", err_log)
                        sys.exit(1)
            case 4:  # Overall Balance Changes per Day
                bal = all_data.bal_chart()
                if bal[0]:
                    check_bal = io.chart_save(bal[1], 
                                                "charts/bal_chart.png")
                    if check_bal[0]:
                        print(check_bal[1])
                        plt.close(check_bal[1][0])
                    else:
                        io.err_handle(check_bal[1], err_log)
                else:
                    force = io.warn_handle(bal[1])
                    if force:
                        print("Returning to analysis menu.")
                    else:
                        io.err_handle("Process aborted.", err_log)
                        sys.exit(1)
            case 5:  # Top 5 Expenses
                top = all_data.top5_chart()
                if top[0]:
                    check_top = io.chart_save(top[1], 
                                                "charts/top5_chart.png")
                    if check_top[0]:
                        print(check_top[1])
                        plt.close(check_top[1][0])
                    else:
                        io.err_handle(check_top[1], err_log)
                else:
                    force = io.warn_handle(top[1])
                    if force:
                        print("Returning to analysis menu.")
                    else:
                        io.err_handle("Process aborted.", err_log)
                        sys.exit(1)
            case _:
                print('That doesn\'t seem to be an option.')
        print('')
        io.print_analysis_menu()
        usr_in = input()

    # Closing
    print("\nThank you for using the expense tracker!\n")
