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