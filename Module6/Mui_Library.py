# Tiffany M. Mui
# Module 6 Assignment - Library Class Module
# CSCI-3025: Python Programming
# Purpose: Library class with associated attributes and methods
# Dependencies: TBD


class Library:
    """Provides library book inventory and patron management"""

    def __init__(self, name = 'Library', phone = None, address = None):
        self.name = name
        self.phone = phone
        self.address = address
        self.books = {}
        self.books_out = {}
        self.patrons = {}