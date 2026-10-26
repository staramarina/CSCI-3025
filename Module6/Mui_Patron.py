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


    def __init__(self, num, last = '', first = '', dob = None, 
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
        self.__dob = dob
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.standing = 'good'
        self.books = {}


    @property
    def dob(self):
        """Used for validated access to patron's date of birth attribute"""
        return self.__dob


    @dob.setter
    def dob(self, value):
        """Used to valid patron's date of birth
        
        Args:
            value: Patron's date of birth in YYYYMMDD string format
        
        Raises:
        """
        if value is None:
            self.__dob = value
        else:
            date = date_format(value, False)
            if not date[1]:
                self.__dob = date[0]
            else:
                raise ValueError(date[0])


    @property
    def phone(self):
        """Used for validated access to patron's phone number attribute"""
        return self.__phone


    @property
    def email(self):
        """Used for validated access to patron's email address attribute"""
        return self.__email


    @property
    def address(self):
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
            True is patron has book, otherwise False
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
        co_len = 3
        if self.book_check(book):
            return (False, 'A copy of this book is already checked out')
        elif limit == len(self.books):
            return (False, f'Cannot exceed checkout limit of {limit}')
        elif (book.hold_check()) and (book.qty <= book.hold_qty):
            return (False, 'This book is currently on hold')
        elif (
            0 == len(book.waitlist)
            or self.card_num == book.waitlist[0]
        ):
            book.qty -= 1
            book_copy = deepcopy(book)
            book_copy.qty = 1
            book_copy.waitlist = []
            book_copy.return_date = datetime.now() + timedelta(weeks=co_len)
            self.books[book.isbn] = book_copy
            if 0 != len(book.waitlist):
                book.waitlist.pop(0)
            return (True, 'Book was successfully checked out')
        elif self.card_num in book.waitlist:
            place = book.waitlist.index(self.card_num)
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
        if self.book_check(book):
            self.books.pop(book.isbn)
            book.qty += 1
            return (True, 'Book successfully returned')
        else:
            return (False, 'That book was not checked out')


    def checkout_extend(self, book):
        """Extends the return date of a book

        Args:
            book: a Book class instance
        
        Returns:
            A 2-tuple with the following elements
                [0]: True if extension was successful, otherwise False
                [1]: Addition information on return condition
        """
        co_len = 3
        if self.book_check(book):
            if (book.hold_check()) and (book.qty <= book.hold_qty):
                return (False, 'Book is on hold, return cannot be extended')
            elif 0 < len(book.waitlist):
                return (False, 'Book is waitlisted, return cannot be extended')
            else:
                self.books[book.isbn].return_date += timedelta(weeks=co_len)
                return (True, 'Return date successfully extended')
        else:
            return (False, 'Book is not currently checked out')


    def waitlist_add(self, book):
        """Adds a patron to the waitlist for a book
           Note: assumes book exists in library database and it's not available
        
        Args:
            book: a Book class instance
        
        Returns:
            A 2-tuple with the following elements
                [0]: True if patron is on the waitlist, otherwise False
                [1]: Index in the waitlist if true, otherwise error message
        """
        if not self.book_check(book):
            if self.card_num in book.waitlist:
                position = book.waitlist.index(self.card_num)
            else:
                book.waitlist.append(self.card_num)
                position = len(book.waitlist) - 1
            return (True, position)
        else:
            return (False, 'You already have that book checked out')


    def checked_out(self):
        """Displays information on all books patron has checked out"""
        if 0 == len(self.books):
            print('No books currently checked out')
        else:
            for book in self.books.values():
                print(book.show_status())


class Educator(Patron):
    """Provides information on and support actions of educators"""


    def __init__(self, num = '0', last = '', first = '', dob = None, 
                 phone = '', email = '', address = '', institution = ''):
        """Initializes an instance of the Patron class
        
        Args:
            num: Unique library card number
            last: Educator's last name
            first: Educator's first name
            dob: Educator's date of birth
            phone: Educator's phone number
            email: Educator's email address
            address: Educator's residential address
            institution: The educator's institution
        
        Returns:
            Educator instance
        """
        super().__init__(num = num, last = last, first = first, dob = dob, 
                         phone = phone, email = email, address = address)
        self.institution = institution
        self.hold_books = {}


    def hold_book(self, book):
        """Checks whether the educator current has a hold on the book
        
        Args:
            book: a Book class instance
        
        Returns:
            A 2-tuple of the following format
                [0]: True if book is on hold and within window, otherwise False
                [1]: Additional information on outcome
        """
        today = datetime.now()
        if 0 == len(self.hold_books):
            return (False, 'You currently have no books on hold')
        elif book.isbn in self.hold_books:
            if today < self.hold_books[book.isbn].hold_start :
                return (False, 'Your hold window has not started')
            elif self.hold_books[book.isbn].hold_end < today:
                return (False, 'Your hold window has ended')
            else:
                qty = self.hold_books[book.isbn].qty
                return (True, qty)
        else:
            return (False, 'You do not have a hold on the book')


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
        limit = 50
        co_len = 6
        if self.book_check(book):
            return (False, 'A copy of this book is already checked out')
        elif limit == len(self.books):
            return (False, f'Cannot exceed checkout limit of {limit}')
        elif (book.hold_check()) and (book.qty <= book.hold_qty):
            hold_flag = self.hold_book(book)
            if hold_flag[0]:
                book.qty -= hold_flag[1]
                book_copy = deepcopy(book)
                book_copy.qty = hold_flag[1]
                book_copy.waitlist = []
                book_copy.return_date = book.hold_end
                self.books[book.isbn] = book_copy
                has_flag = self.book_check(book)
                self.hold_books.pop(book.isbn)
                return (True, 'Book was successfully checked out')
            else:
                return (False, hold_flag[1])
        elif (
            0 == len(book.waitlist)
            or self.card_num == book.waitlist[0]
        ):
            book.qty -= 1
            book_copy = deepcopy(book)
            book_copy.qty = 1
            book_copy.waitlist = []
            book_copy.return_date = datetime.now() + timedelta(weeks=co_len)
            self.books[book.isbn] = book_copy
            if 0 != len(book.waitlist):
                book.waitlist.pop(0)
            return (True, 'Book was successfully checked out')
        elif self.card_num in book.waitlist:
            place = book.waitlist.index(self.card_num)
            return (False, f'You are currently number {place} on the waitlist')
        else:
            return (False, 'Book is not available')


    def checkout_extend(self, book):
        """Extends the return date of a book

        Args:
            book: a Book class instance
        
        Returns:
            A 2-tuple with the following elements
                [0]: True if extension was successful, otherwise False
                [1]: Addition information on return condition
        """
        co_len = 6
        if self.book_check(book):
            if (book.hold_check()) and (book.qty <= book.hold_qty):
                return (False, 'Book is on hold, return cannot be extended')
            elif 0 < len(book.waitlist):
                return (False, 'Book is waitlisted, return cannot be extended')
            else:
                self.books[book.isbn].return_date += timedelta(weeks=co_len)
                return (True, 'Return date successfully extended')
        else:
            return (False, 'Book is not currently checked out')


    def hold_request(self, book, start, end, qty):
        """Places a hold on the requsted book
           Notes: assumes book in library database
                  assumes int and date format checks already run
        
        Args:
            book: a Book class instance
            start: requested hold start date
            end: requested hold end date
            qty: requested hold quantity
        
        Returns:
            A 2-tuple with the following elements
                [0]: True if hold was successful, otherwise False
                [1]: Addition information on return condition
        """
        today = datetime.now()
        if book.isbn in self.hold_books:
            return (False, 'Book is already on hold')
        elif qty > book.tot_qty:
            return (False, 'Cannot hold more than available quantity')
        elif (today > start) or (today > end):
            return (False, 'Cannot hold for past dates')
        elif start > end:
            return (False, 'Cannot set end date before start date')
        else:
            book.hold_start = start
            book.hold_end = end
            book.hold_qty = qty
            book_copy = deepcopy(book)
            book_copy.qty = qty
            self.hold_books[book.isbn] = book_copy
            return (True, 'Book added to hold list')


    def hold_update(self, book, start, end):
        """Updates the hold dates on the requested book
           Notes: assumes book in library database
                  assumes int and date format checks already run
        
        Args:
            book: a Book class instance
            start: updated hold start date
            end: updated hold end date
        
        Returns: 
            A 2-tuple with the following elements
                [0]: True if update was successful, otherwise False
                [1]: Addition information on return condition
        """
        today = datetime.now()
        if book.isbn not in self.hold_books:
            return (False, 'Book is not currently on hold')
        elif (today > start) or (today > end):
            return (False, 'Cannot update for past dates')
        elif start > end:
            return (False, 'Cannot set end date before start date')
        else:
            book.hold_start = start
            book.hold_end = end
            self.hold_books[book.isbn].hold_start = start
            self.hold_books[book.isbn].hold_end = end
            return (True, 'Book hold updated')


    def hold_remove(self, book):
        """Remove the hold on the specified book
           Note: assumes book in library database
        
        Args:
            book: a Book class instance
        
        Returns:
            A 2-tuple with the following elements
                [0]: True if removal was successful, otherwise False
                [1]: Addition information on return condition
        """
        if book.isbn not in self.hold_books:
            return (False, 'Book is not currently on hold')
        else:
            self.hold_books.pop(book.isbn)
            book.hold_start = None
            book.hold_end = None
            book.hold_qty = 0
            return (True, 'Hold removed successfully')