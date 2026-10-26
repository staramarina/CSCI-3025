# Tiffany M. Mui
# Module 6 Assignment - Book Class Module
# CSCI-3025: Python Programming
# Purpose: Book class with associated attributes and methods
# Dependencies: datetime

from datetime import datetime


class Book:
    """Provides information and checks on books"""

    def __init__(self, isbn, author = '',
                 title = '', qty = 1):
        """Initializes an instance of the Book class
        
        Args:
            isbn: ISBN of the book
            author: Author of the book with first name first
            title: Title of the book
            qty: Number of copies the library has available, must be int >= 0
        
        Returns:
            Book instance
        """
        self.isbn = isbn
        self.author = author
        self.title = title
        self.__qty = qty
        self.return_date = None
        self.hold_start = None
        self.hold_end = None
        self.hold_qty = 0
        self.__tot_qty = self.qty
        self.waitlist =  []


    @property
    def qty(self):
        """Used for validated access to book's quantity attribute"""
        return self.__qty


    @property
    def tot_qty(self):
        """Used for validated access to book's total quantity attribute"""
        return self.__tot_qty


    def _val_qty(self, value):
        """Checks quantity value, rejects invalid values
        
        Args:
            value: number of copies in the library, must be int and >= 0

        Raises:
            TypeError: if value is a bool or not an int
            ValueError: if value is less than 0
        """
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError('Quantity must be an integer')
        elif 0 > value:
            raise ValueError('Quantity cannot be negative')
        else:
            return value


    @qty.setter
    def qty(self, value):
        """Sets quantity after validation
        
        Args:
            value: number of copies in the library, must be int and >= 0
        """
        self.__qty = self.__val_qty(value)


    @tot_qty.setter
    def tot_qty(self, value):
        """Sets quantity after validation
        
        Args:
            value: number of copies in the library, must be int and >= 0
        """
        self.__tot_qty = self.__val_qty(value)


    def hold_check(self):
        """Checks whether a book is currently within the hold period
        
        Args:
            None
        
        Returns:
            True if the book is currently on hold, otherwise False
        """
        today = datetime.now()
        if not self.hold_start:
            return False
        elif self.hold_start <= today <= self.hold_end:
            return True
        else:
            return False


    def __str__(self):
        """Provides ISBN, author, title, and quantity information for a book"""
        return(f'ISBN: {self.isbn}, Author: {self.author}, '
               f'Title: {self.title}, Available Quantity: {self.qty}')


    def show_status(self):
        """Provides ISBN, author, title, and 
           return date information for a book"""
        return(f'ISBN: {self.isbn}, '
               f'Author: {self.author}, '
               f'Title: {self.title}, '
               f'Return Date: {self.return_date}')


    def show_hold(self):
        """Provides ISBN, author, title, hold start date, and
           hold end date information for a book"""
        return(f'ISBN: {self.isbn}, '
               f'Author: {self.author}, '
               f'Title: {self.title}, '
               f'Hold Start: {self.hold_start}, '
               f'Hold End: {self.hold_end}')