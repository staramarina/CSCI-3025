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
    print("\nWelcome to the expense tracker!\n")

    # Ask user for their transaction files
    """ # TODO add this back in later when ready to conduct full testing.
    file_list = []
    more_file = "y"
    while more_file in ["Y", "y"]:
        check = io.file_input_handle()
        if check[0]:
            file_list.append(check[1])
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
    df_list = []
    for file in TEST_FILES:  # TODO replace with file_list later
        check = parse.build_dataframe(file)
        if check[0]:  # If dataframe successfully built
            df_list.append(check[1])
        else:  # Error creating dataframe
            io.err_handle(check[1], err_log)
            warn_msg = f"Will drop {file}."
            force = io.warn_handle(warn_msg, err_log)
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
    df_clean = []
    for df in df_list:
        check = parse.clean_dataframe(df, err_log)
        if check[0]:  # If dataframes successfully cleaned
            df_clean.append(check[1])
        else:  # Error cleaning dataframe
            io.err_handle(check[1], err_log)
            warn_msg = f"Will drop data."
            force = io.warn_handle(warn_msg, err_log)
            if force:  # Continue with next data set
                print("Continuing with next data set.")
            else:  # Gracefully terminate the program
                io.err_handle("Process aborted.", err_log)
                sys.exit(1)
    if 0 == len(df_clean):
        print("No useable data. Please restart.")
        sys.exit(1)
    print("Data successfully parsed and cleaned.")

 

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

