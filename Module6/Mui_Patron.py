# Tiffany M. Mui
# Module 6 Assignment - Patron Class Module
# CSCI-3025: Python Programming
# Purpose: Patron and Educator classes with associated attributes and methods
# Dependencies: datetime, Mui_book, Mui_Ancillary


from datetime import datetime, timedelta
from copy import deepcopy
from Mui_Ancillary import date_format


class Parton:
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
        today = datetime.now()
        if 12 > len(self.books):
            if book.hold_start > today or book.hold_end < today:
                if (
                    0 == len(book.waistlist) 
                    or self.card_num == book.waitlist[0]
                ):
                    book.qty -= 1
                    book_copy = deepcopy(book)
                    book_copy.qty = 1
                    book_copy.waitlist = []
                    book_copy.return_date = today + timedelta(weeks=3)
                    self.books.append(book_copy)
                elif self.card_num in book.waitlist:
                    place = book.waitlist(self.card_num)
                    return (False, 
                            f'You are currently number {place} on the waitlist')
                else:
                    return (False, 'Book is waitlisted')
            else: 
                return (False, 'Book is currently on hold')
        else:
            return (False, f'Cannot exceed checkout limit of {limit}')


    def checkout_extend(self, book):
        """Extends the return date of a book
        
        Args:
            book: a Book class instance
        
        Returns:
            True if patron has book, otherwise false
        """
        if book in self.books: # TODO: fix this to account for copy
            self.books[book.isbn].return_date += timedelta(weeks=3)
            return True
        else:
            return False