# Tiffany M. Mui
# Module 6 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: Main program for a library tool
# Dependencies: Mui_Library.py, Mui_Book.py, Mui_Patron.py, Mui_Ancillary,
#               sys
#               see README for full details
# Provided Input Files (required): 
    # testbookdata.txt - real book information from my ebooks
    # testpatrondata.txt - generated using generate-random.org/persons
    # testeducatordata.txt - generated using generate-random.org/persons


import sys
from Mui_Library import Library
from Mui_Book import Book
from Mui_Patron import Patron
from Mui_Ancillary import file_exists, int_check


if __name__ == "__main__":
    # Example library values
    lib_name = 'Mui Mini Library'
    lib_ph = '719-542-7279' # Example only, do not call
    lib_add = '123 S Academy Blvd, Fountain, CO 80819' # Example only
    book_file = 'testbookdata.txt'
    patron_file = 'testpatrondata.txt'
    educator_file = 'testeducatordata.txt'

    # Library instatiation -- only performed once to bring the library online
    mml = Library(lib_name, lib_ph, lib_add)
    book_file_exists = file_exists(book_file)
    patron_file_exists = file_exists(patron_file)
    educator_file_exists = file_exists(educator_file)
    if not book_file_exists[0]:
        print(book_file_exists[1])
        sys.exit(0)
    elif not patron_file_exists[0]:
        print(patron_file_exists[1])
        sys.exit(0)
    elif not educator_file_exists[0]:
        print(educator_file_exists[1])
        sys.exit(0)
    book_reader = open(book_file)
    for line in book_reader:
        if line.isspace():
            continue
        else:
            line = line.strip()
            data = line.split(", ")
            int_flag = int_check(data[3])
            if int_flag[0] and (4 == len(data)):
                book = Book(data[0], data[1], data[2], int_flag[1])
                mml.add_book(book)
            else:
                continue
    book_reader.close()
    patron_reader = open(patron_file)
    for line in patron_reader:
        if line.isspace():
            continue
        else:
            line = line.strip()
            data = line.split(", ")
            if 10 != len(data):
                continue
            else:
                address = (data[6] + ', ' + data[7] + ', ' 
                           + data[8] + ', ' + data[9])
                patron = Patron(data[0], data[1], data[2], data[3],
                                data[4], data[5], address)
                mml.add_patron(patron)
    patron_reader.close()
    educator_reader = open(educator_file)
    # TODO: add bulk import after class is built
    educator_reader.close()

    # Start of library tool
    print('\n')
    print(mml)
    print('\n')
    mml.print_main_menu()
    usr_in = input()
    while 'x' != usr_in:
        main_in = int_check(usr_in)
        if 1 == main_in[1]:
            print('')
            mml.print_staff_menu()
            usr_in = input()
            while 'x' != usr_in:
                staff_in = int_check(usr_in)
                match staff_in[1]:
                    case 1:
                        print('\nPlease enter the following information')
                        isbn = input('ISBN: ')
                        auth = input('Auther: ')
                        title = input('Title: ')
                        qty = input('Quantity: ')
                        qty_chk = int_check(qty)
                        if qty_chk[0]:
                            new_b = Book(isbn, auth, title, qty_chk[1])
                            flag = mml.add_book(new_b)
                            if flag:
                                print('Book added!')
                            else:
                                print('Book could not be added.')
                        else:
                            print('Quantity could not be converted')
                            print(f'Error: {qty_chk[1]}')
                    case 2:
                        # TODO: build Remove a book from the library database
                        print(staff_in[1])
                    case 3:
                        # TODO: build Remove a book from circulation, but not the library
                        print(staff_in[1])
                    case 4:
                        # TODO: build Add a book back into circulation
                        print(staff_in[1])
                    case 5:
                        # TODO: build Add a patron
                        print(staff_in[1])
                    case 6:
                        # TODO: build Remove a patron
                        print(staff_in[1])
                    case _:
                        print('That doesn\'t seem to be an option.')
                print('')
                mml.print_staff_menu()
                usr_in = input()
        elif 2 == main_in[1]:
            print('')
            mml.print_patron_menu()
            usr_in = input()
            while 'x' != usr_in:
                pat_in = int_check(usr_in)
                match pat_in[1]:
                    case 1:
                        # TODO: build Checkout a book
                        print(pat_in[1])
                    case 2:
                        # TODO: build Return a book
                        print(pat_in[1])
                    case 3:
                        # TODO: build Extend return due date on a book
                        print(pat_in[1])
                    case 4:
                        # TODO: build Get added to the waitlist for a book
                        print(pat_in[1])
                    case 5:
                        # TODO: build Request a hold on a book
                        print(pat_in[1])
                    case 6:
                        # TODO: build Extend a hold on a book
                        print(pat_in[1])
                    case 7:
                        # TODO: build Remove a hold on a book
                        print(pat_in[1])
                    case 8:
                        # TODO: build View all checked out books
                        print(pat_in[1])
                    case _:
                        print('That doesn\'t seem to be an option.')
                print('')
                mml.print_patron_menu()
                usr_in = input()
        else:
            print('That doesn\'t seem to be an option.')
            mml.print_main_menu()
            usr_in = input()
        print('')
        mml.print_main_menu()
        usr_in = input()
    print('\nCome back soon!')
