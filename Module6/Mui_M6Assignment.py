# Tiffany M. Mui
# Module 6 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: Main program for a library tool
# Dependencies: Mui_Library.py, Mui_Book.py, Mui_Patron.py
#               see README for full details
# Provided Example Input Files: 
    # Module6/TestData/TBD.txt


from Mui_Library import Library


if __name__ == "__main__":
    lib_name = 'Mui Mini Library'
    lib_ph = '719-542-7279' # Example only, do not call
    lib_add = '123 S Academy Blvd, Fountain, CO 80819' # Example only
    mml = Library(lib_name, lib_ph, lib_add)

    print(mml.name)
    print(mml.phone)
    print(mml.address)

    # TODO: create book instances
    # TODO: add books to library
    # TODO: create patron instances
    # TODO: create educator instances
    # TODO: add patrons and educators to library
    # TODO: create menu