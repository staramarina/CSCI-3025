# Tiffany M. Mui
# Module 6 Assignment - Patron Class Module
# CSCI-3025: Python Programming
# Purpose: Patron and Educator classes with associated attributes and methods
# Dependencies: datetime, copy, Mui_book, Mui_Ancillary


from datetime import datetime, timedelta
from copy import deepcopy
from Mui_Ancillary import date_format


class Patron:
    """Provides information on and support actions of patrons"""


    def __init__(self, num = '0', last = '', first = '', dob = None, 
                 phone = '', email = '', address = ''):
        """Initializes an instance of the Patron class
        
        Args:
            num: Unique library card number
            last: Patron's last name
            first: Patron's first name
            dob: Patron's date of birth
            phone: Patron's phone number
            email: Patron's email address
            address: Patron's residential address
        
        Returns:
            Patron instance
        """
        self.card_num = num
        self.last_name = last
        self.first_name = first
        self.__dob = date_format(dob)
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.standing = 'good'
        self.books = {}


    @property
    def get_dob(self):
        """Used for validated access to patron's date of birth attribute"""
        return self.__dob


    @property
    def get_phone(self):
        """Used for validated access to patron's phone number attribute"""
        return self.__phone


    @property
    def get_email(self):
        """Used for validated access to patron's email address attribute"""
        return self.__email


    @property
    def get_address(self):
        """Used for validated access to patron's address attribute"""
        return self.__address


    def __str__(self):
        """Provides library card number, last name, and first name"""
        return (f'Card #: {self.card_num} - '
                f'{self.last_name}, {self.first_name}')


    def book_check(self, book):
        """Checks whether a patron has already checked out a book
        
        Args:
            book: a Book class instance
        
        Returns:
            A 2-tuple of the following format
                [0]: True is patron has book, otherwise False
                [1]: Index in patron's book list if found, otherwise None
        """
        if book.isbn in self.books:
            return True
        else:
            return False


    def checkout_book(self, book):
        """Checks out a book to a patron
           Note: assumes book_avail from library module was run separately
        
        Args:
            book: a Book class instance
        
        Return:
            A 2-tuple of the following format
                [0]: True if book checkout was successful, otherwise False
                [1]: Additional information on outcome
        """
        limit = 12
        has_flag = self.book_check(book)
        if has_flag:
            return (False, 'A copy of this book is already checked out')
        elif 12 == len(self.books):
            return (False, f'Cannot exceed checkout limit of {limit}')
        elif book.hold_check():
            return (False, 'This book is currently on hold')
        elif (
            0 == len(book.waitlist)
            or self.card_num == book.waitlist[0]
        ):
            book.qty -= 1
            book_copy = deepcopy(book)
            book_copy.qty = 1
            book_copy.waitlist = []
            book_copy.return_date = datetime.now() + timedelta(weeks=3)
            self.books[book_copy.isbn] = book_copy
            has_flag = self.book_check(book)
            if has_flag:
                if 0 != len(book.waitlist):
                    book.waitlist.pop(0)
                return (True, 'Book was successfully checked out')
            else:
                return (False, 'Book could not be checked out')
        elif self.card_num in book.waitlist:
            place = book.waitlist(self.card_num)
            return (False, f'You are currently number {place} on the waitlist')
        else:
            return (False, 'Book is currently waitlisted')


    def return_book(self, book):
        """Returns a book back to the library
           Note: assumes book exists in library database
        
        Args:
            book: a Book class instance
        
        Returns:
            A 2-tuple with the following elements
                [0]: True if return was successful, otherwise False
                [1]: Addition information on return condition
        """
        match = self.book_check(book)
        if match:
            book_return = self.books.pop(book.isbn)
            update = self.book_check(book_return)
            if update:
                return (False, 'Failed to return book')
            else:
                qty_orig = book.qty
                book.qty += 1
                qty_new = book.qty
                if qty_new > qty_orig:
                    return (True, 'Book returned successfully')
                else:
                    return (False, 'Failed to update library inventory')
        else:
            return (False, 'That book was not checked out')


    def checkout_extend(self, book):
        """Extends the return date of a book
           Note: assumes patron has book
        
        Args:
            book: a Book class instance
        
        Returns:
            True if patron has book, otherwise false
        """
        match = self.book_check(book)
        if book.hold_check():
            return (False, 'Book is on hold, checkout cannot be extended')
        elif 0 < len(book.waitlist):
            return (False, 'Book is waitlisted, checkout cannot be extended')
        elif match:
            self.books[book.isbn].return_date += timedelta(weeks=3)
            return (True, 'Return date successfully extended')
        else:
            return (False, 'Book is not currently checked out')


    def waitlist_add(self, book):
        """Adds a patron to the waitlist for a book
        
        Args:
            book: a Book class instance
        
        Returns:
            position: the patron's index in the waitlist
        """
        if self.card_num in book.waitlist:
            position = book.waitlist.index(self.card_num)
        else:
            book.wailist.append(self.card_num)
            position = len(book.waitlist) - 1
        return position


    def checked_out(self):
        """Displays information on all books patron has checked out"""
        if 0 == len(self.books):
            print('No books currently checked out')
        else:
            for book in self.books.values():
                print(book.show_status())