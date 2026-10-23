# Tiffany M. Mui
# Module 6 Assignment - Library Class Module
# CSCI-3025: Python Programming
# Purpose: Library class with associated attributes and methods
# Dependencies: TBD


class Library:
    """Provides library book inventory and patron management"""

    def __init__(self, name = 'Library', phone = None, address = None):
        """Initializes an instance of a Library
        
        Args: 
            name: Name of the library
            phone: Phone number to call the library
            address: Address to visit the library

        Returns:
            Library instance
        """
        self.name = name
        self.phone = phone
        self.address = address
        self.books = {}
        self.books_out = {}
        self.patrons = {}


    def book_exists(self, book):
        """Checks whether a book exists in the circulation inventory
        
        Args:
            book: a Book class instance
        
        Returns:
            True if book in library, otherwise False
        """
        if book.isbn in self.books:
            return True
        else:
            return False


    def add_book(self, book):
        """Adds a Book instance to the library inventory
        
        Args: 
            book: a Book class instance
        
        Returns:
            None
        """
        if self.book_exists(self, book):
            self.books[book.isbn].qty += 1
        else:
            self.books[book.isbn] = book


    def remove_book(self, book):
        """Remove a single Book instance from the library altogether
        
        Args:
            book: a Book class instance
        
        Returns:
            True if book in library, otherwise False
        """
        if self.book_exists(self.book):
            if 1 < self.books[book.isbn].qty:
                self.books[book.isbn].qty -= 1
                return True
            elif 1 == self.books[book.isbn].qty:
                self.books[book.isbn].pop()
                return True
            else:
                return False
        else:
            return False


    def decirc_book(self, book):
        """Remove a book from the circulation inventory and
           add it to the out of circulation inventory
        
        Args: 
            book: a Book class instance

        Returns:
            True if book in library, otherwise False
        """
        if self.remove_book(self, book):
            if book.isbn in self.books_out:
                self.books_out[book.isbn].qty += 1
            else:
                self.books_out[book.isbn] = book
            return True
        else:
            return False


    def recirc_book(self, book):
        """Adds a book back into the circulation inventory
           from the decirculation inventory
        
        Args:
            book: a Book class instance
        
        Returns:
            True if book in library, otherwise False
        """
        if book.isbn in self.books_out:
            if 1 < self.books_out[book.isbn].qty:
                self.books_out[book.isbn].qty -= 1
                self.add_book(self, book)
                return True
            elif 1 == self.books_out[book.isbn].qty:
                self.books_out[book.isbn].pop()
                self.add_book(self, book)
                return True
            else:
                return False
        else:
            return False


    def patron_exists(self, patron):
        """Checks whether a patron exists in the library database
        
        Args:
            patron: a Patron or Educator class instance
        
        Returns:
            True if patron exists, otherwise False
        """
        if patron.card_num in self.patrons:
            return True
        else:
            return False


    def add_patron(self, patron):
        """Adds a Patron instance to the library
        
        Args:
            patron: a Patron or Educator class instance
        
        Returns:
            False if patron already exists, otherwise True
        """
        if not self.patron_exists(self, patron):
            self.patrons[patron.card_num] = patron
            return True
        else:
            return False


    def remove_patron(self, patron):
        """Removes a Patron instance from the library
        
        Args:
            patron: a Patron or Educator class instance
        
        Returns:
            True if patron exists, otherwise False
        """
        if self.patron_exists(self, patron):
            self.patrons[patron.card_num].pop()
            return True
        else:
            return False

