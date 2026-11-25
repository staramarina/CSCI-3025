# Tiffany M. Mui
# Module 9 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: Personal Expense Tracker
# Dependencies:
#   Standard: datetime
#   External: pandas, matplotlib, seaborn
#   Custom: Mui_Ancillary.py, Mui_IO.py,
#           Mui_Parser.py, Mui_Statement.py


import sys
import Mui_Ancillary as aux
import Mui_IO as io
import Mui_Parser as parse
import Mui_Statement as stmnt


TEST_FILES = [
    'data/bofa_checking_example.csv',
    'data/chase_checking_example.csv',
    'data/chase_credit_example.csv',
    'data/citibank_checking_example.csv',
    'data/citibank_credit_example.csv',
    'data/sample-bank-transactions.csv',
    'data/SCU_checking_example.csv',
    'data/SCU_credit_example.csv',
    'data/USAA_checking_example.csv',
    'data/USAA_credit_example.csv',
    'data/wellsfargo_checking_example.csv'
]


if __name__ == "__main__":
    # Setup
    err_log = "Mui_M9_Log.txt"
    io.log_setup(err_log)
    file_list = []

    # Ask user for their transaction files
    """ # TODO add this back in later when ready to conduct full testing.
    more_file = "y"
    while more_file in ["Y", "y"]:
        check = io.file_input_handle()
        if check[0]:
            file_list.append(check[1])
            more_file = input("Would you like to include another file (Y/N): ")
        else:
            io.err_handle(check[1], err_log)
            more_file = input("Would you like to try again (Y/N): ")
    """
    # Data Parsing -- Actual functions in parser module
    df_list = []
    for file in TEST_FILES: # TODO change to file_list later
        check = parse.build_dataframe(file)
        if check[0]:
            df_list.append(check[1])
        else:
            force = io.warn_handle(check[1], err_log)
            if force:
                print("Continuing with next data set.")
            else:
                sys.exit(1)
    if 0 == len(df_list):
        print("No useable files. Please restart.")
        sys.exit(1)
    df_clean = []
    for df in df_list:
        check = parse.clean_dataframe(df, err_log)
        if check[0]:
            df_clean.append(check[1])
        else:
            force = io.warn_handle(check[1], err_log)
            if force:
                print("Continuing with next data set.")
            else:
                sys.exit(1)
    if 0 == len(df_clean):
        print("No useable data. Please restart.")
        sys.exit(1)


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



    # TODO Temporary data dump for testins
    with open('test_dump.txt', "a") as f: 
        for df in df_clean:
            f.write(df.to_string(header=True, index=True)) # dumps data from feed endpoint
            f.write('\n\n') # extra lines for readability

