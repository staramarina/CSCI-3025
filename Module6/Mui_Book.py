# Tiffany M. Mui
# Module 6 Assignment - Book Class Module
# CSCI-3025: Python Programming
# Purpose: Book class with associated attributes and methods
# Dependencies: TBD


class Book:
    """Provides information and checks on books"""

    def __init__(self, isbn = '0', author = '',
                 title = '', qty = 1):
        """Initializes an instance of the Book class
        
        Args:
            isbn: ISBN of the book
            author: Author of the book with first name first
            title: Title of the book
            qty: Number of copies the library has available
        
        Returns:
            Book instance
        """
        self.isbn = isbn
        self.author = author
        self.title = title
        self.qty = qty
        self.return_date = None
        self.hold_start = None
        self.hold_end = None
        self.waitlist =  []


    def show_info(self):
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