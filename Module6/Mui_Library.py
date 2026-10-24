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


    def book_in_exists(self, book):
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


    def book_out_exists(self, book):
        """Checks whether a book exists in the non-circulation inventory
        
        Args: 
            book: a Book class instance
        
        Returns:
            True if book in library, otherwise False
        """
        if book.isbn in self.books_out:
            return True
        else:
            return False


    def add_book(self, book):
        """Adds a Book instance to the library inventory
        
        Args: 
            book: a Book class instance
        
        Returns:
            True if book successfully added, otherwise False
        """
        if self.book_in_exists(self, book):
            qty_orig = self.books[book.isbn].qty
            self.books[book.isbn].qty += 1
            qty_new = self.books[book.isbn].qty
            if qty_new > qty_orig:
                return True
            else:
                return False
        else:
            self.books[book.isbn] = book
            if self.book_in_exists(self, book):
                return True
            else:
                return False


    def remove_book(self, book):
        """Remove a single Book instance from the library altogether
        
        Args:
            book: a Book class instance
        
        Returns:
            True if book removed successfully, otherwise False
        """
        if self.book_in_exists(self, book):
            qty_orig = self.books[book.isbn].qty
            if 1 < qty_orig:
                self.books[book.isbn].qty -= 1
                qty_new = self.books[book.isbn].qty
            elif 1 == qty_orig:
                self.books[book.isbn].pop()
            else:
                return False
            if qty_new < qty_orig:
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
            True if book was successfully moved to decirculation inventory, 
                otherwise False
        """
        if self.remove_book(self, book):
            if self.book_out_exists(self, book):
                qty_out_orig = self.books_out[book.isbn].qty
                self.books_out[book.isbn].qty += 1
                qty_out_new = self.books_out[book.isbn].qty
                if (qty_out_orig < qty_out_new):
                    return True
                else:
                    return False
            else:
                self.books_out[book.isbn] = book
                if self.book_out_exists(self, book):
                    return True
                else:
                    return False
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
        if self.book_out_exists(self, book):
            qty_orig = self.books_out[book.isbn].qty
            if 1 < qty_orig:
                self.books_out[book.isbn].qty -= 1
                qty_new = self.books_out[book.isbn].qty
                if (qty_new < qty_orig) and self.add_book(self, book):
                    return True
                else:
                    return False
            if 1 == qty_orig:
                self.books_out[book.isbn].pop()
                if self.book_out_exists(self, book):
                    return False
                elif self.add_book(self, book):
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


    def show_books(self):
        """Prints all books in the library to the console"""
        for book in self.books.values():
            print(book.show_info()) # TODO: check this after implementation


    def search_isbn(self, search):
        """Prints books information for the given ISBN if it exists
        
        Args:
            search: ISBN search term
        
        Returns:
            None
        """
        book = self.books.get(search)
        if book is not None:
            print(self.books[search].show_info()) # TODO : check this after implementation
        else:
            print('That book is not available.')


    def search_author(self, search):
        """Prints book information written by given author if they exist
        
        Args:
            search: Author name, not case sensitive, can be partial
        
        Returns:
            None
        """
        count = 0
        for isbn, book in self.books:
            if search.lower() in book.author.lower():
                print(self.books[isbn].show_info()) # TODO : check this after implementation
                count += 1
        if 0 == count:
            print('No books with that author found.')


    def search_title(self, search):
        """Prints book information with given title if they exist
        
        Args:
            search: Title of book, not case sensitive, can be partial

        Returns:
            None
        """
        count = 0
        for isbn, book in self.books:
            if search.lower() in book.title.lower():
                print(self.books[isbn].show_info()) # TODO : check this after implementation
                count += 1
        if 0 == count:
            print('No books with that title found.')