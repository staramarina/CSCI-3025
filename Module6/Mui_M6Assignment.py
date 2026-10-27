# Tiffany M. Mui
# Module 6 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: Main program for a library tool
# Dependencies: Mui_Library.py, Mui_Book.py, Mui_Patron.py, Mui_Ancillary,
#               sys, datetime, copy
#               see README for full details
# Provided Input Files (required): 
    # testbookdata.txt - real book information from my ebooks
    # testpatrondata.txt - generated using generate-random.org/persons
    # testeducatordata.txt - generated using generate-random.org/persons


import sys
from Mui_Library import Library
from Mui_Book import Book
from Mui_Patron import Patron, Educator
from Mui_Ancillary import file_exists, int_check, date_format


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
                try:
                    book = Book(data[0], data[1], data[2], int_flag[1])
                except (TypeError, ValueError) as err:
                    book_reader.close()
                    print(err)
                    sys.exit(0)
                else:
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
                try:
                    patron = Patron(data[0], data[1], data[2], data[3],
                                    data[4], data[5], address)
                except ValueError as err:
                    patron_reader.close()
                    print(err)
                    sys.exit(0)
                else:
                    mml.add_patron(patron)
    patron_reader.close()
    educator_reader = open(educator_file)
    for line in educator_reader:
        if line.isspace():
            continue
        else:
            line = line.strip()
            data = line.split(", ")
            if 11 != len(data):
                continue
            else:
                address = (data[6] + ', ' + data[7] + ', ' 
                           + data[8] + ', ' + data[9])
                try:
                    educator = Educator(data[0], data[1], data[2], data[3],
                                    data[4], data[5], address, data[10])
                except ValueError as err:
                    educator_reader.close()
                    print(err)
                    sys.exit(0)
                else:
                    mml.add_patron(educator)
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
                        auth = input('Author: ')
                        title = input('Title: ')
                        qty = input('Quantity: ')
                        if '' == qty:
                            qty = None
                        qty_chk = int_check(qty)
                        if qty_chk[0] or None == qty:
                            try:
                                new_b = Book(isbn, auth, title, qty_chk[1])
                            except (TypeError, ValueError) as err:
                                print(err)
                            else:
                                flag = mml.add_book(new_b)
                                if flag:
                                    print('Book added!')
                                else:
                                    print('Book could not be added.')
                        else:
                            print('Quantity could not be converted')
                            print(f'Error: {qty_chk[1]}')
                    case 2:
                        print('Please enter the ISBN ' \
                              'of the book you want to remove')
                        isbn = input()
                        book = mml.find_book(isbn)
                        if book:
                            flag = mml.remove_book(book)
                            if flag:
                                print('Book removed successfully!')
                            else:
                                print('Error removing book, please try again')
                        else:
                            print('Book is not in the database.')
                    case 3:
                        print('Please enter the ISBN of the book you ' \
                              'want to remove from circulation')
                        isbn = input()
                        book = mml.find_book(isbn)
                        if book:
                            flag = mml.decirc_book(book)
                            if flag:
                                print('Book removed from circulation!')
                            else:
                                print('Error moving book, please try again')
                        else:
                            print('Book is not in the database.')
                    case 4:
                        print('Please enter the ISBN of the book you ' \
                              'want to return to circulation')
                        isbn = input()
                        book = mml.books_out.get(isbn)
                        if book:
                            flag = mml.recirc_book(book)
                            if flag:
                                print('Book returned to circulation!')
                            else:
                                print('Error moving book, please try again')
                        else:
                            print('Book is not in the database.')
                    case 5:
                        print('')
                        mml.print_type_menu()
                        usr_in = input()
                        if 'x' == usr_in:
                            break
                        type_in = int_check(usr_in)
                        if 1 == type_in[1]:
                            print('')
                            data = mml.patron_create_prompt()
                            try:
                                patron = Patron(*data)
                            except ValueError as err:
                                print(err)
                            else:
                                flag = mml.add_patron(patron)
                                if flag:
                                    print('\nThe following patron was added')
                                    print(patron)
                                else:
                                    print('\nThat card number already exists')
                        elif 2 == type_in[1]:
                            print('')
                            data = mml.patron_create_prompt()
                            inst = input('Patron\'s institution: ')
                            try:
                                educator = Educator(*data, inst)
                            except ValueError as err:
                                print(err)
                            else:
                                flag = mml.add_patron(educator)
                                if flag:
                                    print('\nThe following educator was added')
                                    print(educator)
                                else:
                                    print('\nThat card number already exists')
                        else:
                            print('That doesn\'t seem to be an option.')
                    case 6:
                        print('\nPlease enter the card number of the patron ' \
                              'you would like to remove')
                        card = input()
                        patron = mml.find_patron(card)
                        if not patron:
                            print('Account not found.')
                        else:
                            mml.remove_patron(patron)
                            print('The following patron was removed')
                            print(patron)
                    case _:
                        print('That doesn\'t seem to be an option.')
                print('')
                mml.print_staff_menu()
                usr_in = input()
        elif 2 == main_in[1]:
            print('\nPlease enter your library card number')
            card = input()
            patron = mml.find_patron(card)
            if not patron:
                print('Account not found. Please consult staff.')
                print('')
                mml.print_main_menu()
                usr_in = input()
                continue
            print('')
            mml.print_patron_menu()
            usr_in = input()
            while 'x' != usr_in:
                pat_in = int_check(usr_in)
                match pat_in[1]:
                    case 1:
                        print('\nPlease enter the ISBN of the book you would ' \
                              'like to checkout')
                        isbn = input()
                        book = mml.find_book(isbn)
                        if book and mml.book_avail(book):
                            flag = patron.checkout_book(book)
                            print(flag[1])
                        elif book:
                            print('No copies available.')
                            print('Select option 4 to be added to the waitlist')
                        else:
                            print('Book not found.')
                    case 2:
                        print('\nPlease enter the ISBN of the book you would ' \
                              'like to return')
                        isbn = input()
                        book = mml.find_book(isbn)
                        if book:
                            flag = patron.return_book(book)
                            print(flag[1])
                        else:
                            print('Book is not in the library database.')
                    case 3:
                        print('\nPlease enter the ISBN of the book you would ' \
                              'like to extend checkout')
                        isbn = input()
                        book = mml.find_book(isbn)
                        if book:
                            flag = patron.checkout_extend(book)
                            print(flag[1])
                        else:
                            print('Book is not in the library database.')
                    case 4:
                        print('\nPlease enter the ISBN of the book you would ' \
                              'like to be added to the waitlist for')
                        isbn = input()
                        book = mml.find_book(isbn)
                        if mml.book_avail(book):
                            print('Book is available for checkout.')
                            print('Select option 1 to checkout book.')
                        elif book:
                            flag = patron.waitlist_add(book)
                            if flag[0]:
                                print(f'You are number {flag[1] + 1} '
                                      f'on the waitlist')
                            else:
                                print(flag[1])
                        else:
                            print('Book is not in the library database.')
                    case 5:
                        print('\nPlease enter the ISBN of the book you would ' \
                              'like to place a hold')
                        isbn = input()
                        book = mml.find_book(isbn)
                        ed_flag = isinstance(patron, Educator)
                        if ed_flag and book:
                            data = mml.ed_hold_prompt()
                            qty_in = input('Quantity: ')
                            start = date_format(data[0], True)
                            end = date_format(data[1], True)
                            qty = int_check(qty_in)
                            if not start[0]:
                                print(start[1])
                            elif not end[0]:
                                print(end[1])
                            elif not qty[0]:
                                print('Invalid quantity')
                            elif 1 > qty[1]:
                                print('Quantity cannot be negative or zero')
                            else:
                                flag = patron.hold_request(book, start[0], 
                                                           end[0], qty[1])
                                print(flag[1])
                        elif ed_flag:
                            print('Book does not exist in the library database')
                        else:
                            print('Only educator accounts can process holds')
                    case 6:
                        print('\nPlease enter the ISBN of the book you would ' \
                              'like to update the hold')
                        isbn = input()
                        book = mml.find_book(isbn)
                        ed_flag = isinstance(patron, Educator)
                        if ed_flag and book:
                            data = mml.ed_hold_prompt()
                            start = date_format(data[0], True)
                            end = date_format(data[1], True)
                            if not start[0]:
                                print(start[1])
                            elif not end[0]:
                                print(end[1])
                            else:
                                flag = patron.hold_update(book, start[0], 
                                                          end[0])
                                print(flag[1])
                        elif ed_flag:
                            print('Book does not exist in the library database')
                        else:
                            print('Only educator accounts can process holds')
                    case 7:
                        print('\nPlease enter the ISBN of the book you would ' \
                              'like to remove the hold')
                        isbn = input()
                        book = mml.find_book(isbn)
                        ed_flag = isinstance(patron, Educator)
                        if ed_flag and book:
                            flag = patron.hold_remove(book)
                            print(flag[1])
                        elif ed_flag:
                            print('Book does not exist in the library database')
                        else:
                            print('Only educator accounts can process holds')
                    case 8:
                        print('\nYour checked out books:')
                        patron.checked_out()
                    case _:
                        print('That doesn\'t seem to be an option.')
                print('')
                mml.print_patron_menu()
                usr_in = input()
        elif 3 == main_in[1]:
            print('')
            mml.print_search_menu()
            usr_in = input()
            while 'x' != usr_in:
                srch_in = int_check(usr_in)
                match srch_in[1]:
                    case 1:
                        print('\n')
                        for book in mml.books.values():
                            print(book)
                        print('\n')
                    case 2:
                        print('Please enter the ISBN of the book you would ' \
                              'like to find')
                        isbn = input()
                        print(f'\nSearch for "{isbn}" yielded the following:')
                        mml.search_isbn(isbn)
                    case 3:
                        print('Please enter the author of the book you would ' \
                              'like to find')
                        auth = input()
                        print(f'\nSearch for "{auth}" yielded the following:')
                        mml.search_author(auth)
                    case 4:
                        print('Please enter the title of the book you would ' \
                              'like to find')
                        title = input()
                        print(f'\nSearch for "{title}" yielded the following:')
                        mml.search_title(title)
                    case _:
                        print('That doesn\'t seem to be an option.')
                print('')
                mml.print_search_menu()
                usr_in = input()
        else:
            print('That doesn\'t seem to be an option.')
            mml.print_main_menu()
            usr_in = input()
        print('')
        mml.print_main_menu()
        usr_in = input()
    print('\nCome back soon!\n')
