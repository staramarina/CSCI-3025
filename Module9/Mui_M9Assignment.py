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
    USAA_CHECK: True,
    #USAA_CREDIT: True,
    #SAFE_CREDIT: True
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
    print("\nBuilding data frames.")
    df_list = {}
    df_pop_ls = []
    for file in REAL_FILES:  # TODO replace with file_list later
        check = parse.build_dataframe(file)
        if check[0]:  # If dataframe successfully built
            df_list[file] = check[1]
        else:  # Error creating dataframe
            io.err_handle(check[1], err_log)
            warn_msg = f"Will drop {file}."
            force = io.warn_handle(warn_msg)
            if force:  # Continue with next data set
                df_pop_ls.append(file)  # Add to removal flagged list
                print("Continuing with next data set.")
            else:  # Gracefully terminate the program
                io.err_handle("Process aborted.", err_log)
                sys.exit(1)
    for file in df_pop_ls:  # Removal of flagged files
        df_list.pop(file)
    df_pop_ls.clear()
    if 0 == len(df_list):
        print("No useable files. Please restart.")
        sys.exit(1)
    print("Data frame(s) created.")


    # TODO Temporary data dump for testins
    with open('test_dump.txt', "w") as f: 
        f.write('------------------------ORIGINAL DATAFRAMES------------------------\n')
        for df in df_list.values(): # pre-cleaning print
            f.write(df.to_string(header=True, index=True)) # dumps data from feed endpoint
            f.write('\n\n') # extra lines for readability


    # Parse/clean dataframes
    print("\nParsing and cleaning data.")
    df_clean = {}
    for file, df in df_list.items():
        check = parse.clean_dataframe(df, err_log)
        if check[0]:  # If dataframes successfully cleaned
            df_clean[file] = check[1]
        else:  # Error cleaning dataframe
            io.err_handle(check[1], err_log)
            warn_msg = f"Will drop data."
            force = io.warn_handle(warn_msg)
            if force:  # Continue with next data set
                df_pop_ls.append(file)  # Add to removal flagged list
                print("Continuing with next data set.")
            else:  # Gracefully terminate the program
                io.err_handle("Process aborted.", err_log)
                sys.exit(1)
    for file in df_pop_ls:  # Removal of flagged files
        df_list.pop(file)
    df_pop_ls.clear()
    if 0 == len(df_clean):
        print("No useable data. Please restart.")
        sys.exit(1)
    print("Data successfully parsed and cleaned.")


    # TODO Temporary data dump for testins
    with open('test_dump.txt', "a") as f: 
        f.write('------------------------CLEAN DATAFRAMES------------------------\n')
        for df in df_clean.values(): # pre-classes print
            f.write(df.to_string(header=True, index=True)) # dumps data
            f.write('\n\n') # extra lines for readability


    # Create a list of statement class instances
    df_class = []
    for file, df in df_clean.items():
        statement = stmnt.Statement(df, file)  # TODO add validation check, wrap in try/except
        df_class.append(statement)


    # TODO Temporary data dump for testins
    with open('test_dump.txt', "a") as f: 
        f.write('------------------------CLASSES------------------------\n')
        for data in df_class:  # post-classes print
            f.write(str(data))
            f.write('\n\n') # extra lines for readability


    # Add all class instances together into a single class instance
    all_data = deepcopy(df_class[0])
    for statement in df_class[1:]:
        all_data += statement


    # TODO Temporary data dump for testins
    with open('test_dump.txt', "a") as f: 
        f.write('------------------------COMBINED------------------------\n')
        f.write(str(all_data))  #post combined print


    # Analysis
    # TODO print analysis menu -- call from io
    # TODO check user input with int_check -- call from aux
    # TODO call analysis method -- from stmnt

    # Spend analysis
    #spend = all_data.spend_chart()
    #check_spend = io.chart_save(spend, "charts/spend_chart.png")

    # Category analysis
    #check_cat = all_data.cat_chart()
    #if check_cat[0]:
    #    chart_check = io.chart_save(check_cat[1], "charts/cat_chart.png")

    # Description analysis
    #check_des = all_data.descript_chart()
    #if check_des[0]:
    #    chart_check = io.chart_save(check_des[1], "charts/descript_chart.png")

    # Balance analysis
    #check_bal = all_data.bal_chart()
    #if check_bal[0]:
    #    chart_check = io.chart_save(check_bal[1], "charts/bal_chart.png")

    # Top 5 analysis
    check_top = all_data.top5_chart()
    if check_top[0]:
        chart_check = io.chart_save(check_top[1], "charts/top5_chart.png")

    # TODO print results
    # TODO ask if user wants another analysis, repeat until N/n

    # Closing
    # TODO program closing message(s)


