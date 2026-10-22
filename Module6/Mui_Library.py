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