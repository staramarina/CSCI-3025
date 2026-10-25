# Tiffany M. Mui
# Module 6 Assignment - Library Class Module
# CSCI-3025: Python Programming
# Purpose: Library class with associated attributes and methods
# Dependencies: Mui_Book, Mui_Patron


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


    def find_book(self, isbn):
        """Finds and returns a book with the specified ISBN
        
        Args:
            isbn: the ISBN of the book to find
        
        Returns:
            book: a Book class instance
        """
        book = self.books.get(isbn)
        return book


    def add_book(self, book):
        """Adds a Book instance to the library inventory
        
        Args: 
            book: a Book class instance
        
        Returns:
            True if book successfully added, otherwise False
        """
        if self.book_in_exists(book):
            qty_orig = self.books[book.isbn].qty
            self.books[book.isbn].qty += 1
            qty_new = self.books[book.isbn].qty
            if qty_new > qty_orig:
                return True
            else:
                return False
        else:
            self.books[book.isbn] = book
            if self.book_in_exists(book):
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
        if self.book_in_exists(book):
            qty_orig = self.books[book.isbn].qty
            if 1 < qty_orig:
                self.books[book.isbn].qty -= 1
                qty_new = self.books[book.isbn].qty
                if qty_new < qty_orig:
                    return True
                else:
                    return False
            elif 1 == qty_orig:
                self.books.pop(book.isbn)
                if self.book_in_exists(book):
                    return False
                else:
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
        if self.remove_book(book):
            if self.book_out_exists(book):
                qty_out_orig = self.books_out[book.isbn].qty
                self.books_out[book.isbn].qty += 1
                qty_out_new = self.books_out[book.isbn].qty
                if (qty_out_orig < qty_out_new):
                    return True
                else:
                    return False
            else:
                self.books_out[book.isbn] = book
                if self.book_out_exists(book):
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
            True if book successfully moved to circulation library, 
                otherwise False
        """
        if self.book_out_exists(book):
            qty_orig = self.books_out[book.isbn].qty
            if 1 < qty_orig:
                self.books_out[book.isbn].qty -= 1
                qty_new = self.books_out[book.isbn].qty
                if (qty_new < qty_orig) and self.add_book(book):
                    return True
                else:
                    return False
            if 1 == qty_orig:
                self.books_out.pop(book.isbn)
                if self.book_out_exists(book):
                    return False
                elif self.add_book(book):
                    return True
                else:
                    return False
        else:
            return False


    def book_avail(self, book):
        """Determines whether a book is available for checkout
        
        Args:
            book: a Book class instance
        
        Returns:
            True if quantity in library is at least one, otherwise False
        """
        if self.book_in_exists(book):
            if 1 <= self.books[book.isbn].qty:
                return True
            else:
                return False
        else:
            return False


    def find_patron(self, card):
        """Finds a patron record from their library card number
        
        Args:
            card: library card number as a string
        
        Returns:
            patron: a Patron or Educator class instance
        """
        patron = self.patrons.get(card)
        return patron


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
        if self.patron_exists(patron):
            return False
        else:
            self.patrons[patron.card_num] = patron
            return True


    def remove_patron(self, patron):
        """Removes a Patron instance from the library
        
        Args:
            patron: a Patron or Educator class instance
        
        Returns:
            True if patron exists, otherwise False
        """
        if self.patron_exists(patron):
            self.patrons[patron.card_num].pop()
            return True
        else:
            return False


    def menu_bound_check(self, select = 0, type = 0):
        """Checks whether the selection from the menu is within bounds
        
        Args:
            select: selection from the user, assumes int
            type: type of menu that is being checked
                0 for main
                1 for staff
                2 for patron
                3 for search
        
        Returns:
            True if within bounds, otherwise False
        """
        if 0 == type:
            if 0 < select <= 3:
                return True
            else:
                return False
        elif 1 == type:
            if 0 < select <= 6:
                return True
            else:
                return False
        elif 2 == type:
            if 0 < select <= 8:
                return True
            else:
                return False
        elif 3 == type:
            if 0 < select <= 4:
                return True
            else:
                return False
        else:
            return False


    def print_main_menu(self):
        """Prints the library main menu to the console"""
        print('Please select one of the following options:')
        print('1 -- Staff Login')
        print('2 -- Card Holder Login')
        print('3 -- Search Library Database')
        print('x -- Quit')


    def print_staff_menu(self):
        """Prints the library staff menu to the console"""
        print('Please select one of the following options:')
        print('1 -- Add a book to the library database')
        print('2 -- Remove a book from the library database')
        print('3 -- Remove a book from circulation, but not the library')
        print('4 -- Add a book back into circulation')
        print('5 -- Add a patron')
        print('6 -- Remove a patron')
        print('x -- Quit')


    def print_patron_menu(self):
        """Prints the patron menu to the console"""
        print('Please select one of the following options:')
        print('1 -- Checkout a book')
        print('2 -- Return a book')
        print('3 -- Extend return due date on a book')
        print('4 -- Get added to the waitlist for a book')
        print('5 -- Request a hold on a book')
        print('6 -- Extend a hold on a book')
        print('7 -- Remove a hold on a book')
        print('8 -- View all checked out books')
        print('x -- Quit')


    def print_search_menu(self):
        """Prints the search menu to the console"""
        print('Please select one of the following options:')
        print('1 -- Show all books')
        print('2 -- Search by ISBN')
        print('3 -- Search by author')
        print('4 -- Search by title')
        print('x -- Quit')


    def __str__(self):
        """Provides library name, phone number, and address information"""
        return (f'{self.name}\n{self.phone}\n{self.address}')


    def show_books(self):
        """Prints all books in the library to the console"""
        for book in self.books.values():
            print(book)


    def search_isbn(self, search):
        """Prints books information for the given ISBN if it exists
        
        Args:
            search: ISBN search term
        
        Returns:
            None
        """
        book = self.books.get(search)
        if book is not None:
            #print(self.books[search].show_info()) # TODO : FIX THIS
            print(book)
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
        for book in self.books.values():
            if search.lower() in book.author.lower():
                print(book)
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
        for book in self.books.values():
            if search.lower() in book.title.lower():
                print(book)
                count += 1
        if 0 == count:
            print('No books with that title found.')