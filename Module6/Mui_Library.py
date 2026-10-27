# Tiffany M. Mui
# Module 6 Assignment - Library Class Module
# CSCI-3025: Python Programming
# Purpose: Library class with associated attributes and methods
# Dependencies: Mui_Book, Mui_Patron, copy


from copy import deepcopy


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
            tot_qty_orig = self.books[book.isbn].tot_qty
            qty_orig = self.books[book.isbn].qty
            self.books[book.isbn].tot_qty += 1
            self.books[book.isbn].qty += 1
            tot_qty_new = self.books[book.isbn].tot_qty
            qty_new = self.books[book.isbn].qty
            if (qty_orig < qty_new) and (tot_qty_orig < tot_qty_new):
                return True
            else:
                return False
        else:
            self.books[book.isbn] = book
            return True



    def remove_book(self, book):
        """Remove a single Book instance from the library altogether
        
        Args:
            book: a Book class instance
        
        Returns:
            True if book removed successfully, otherwise False
        """
        if self.book_in_exists(book):
            tot_qty_orig = self.books[book.isbn].tot_qty
            qty_orig = self.books[book.isbn].qty
            if (1 < tot_qty_orig) and (1 < qty_orig):
                self.books[book.isbn].tot_qty -= 1
                self.books[book.isbn].qty -= 1
                tot_qty_new = self.books[book.isbn].tot_qty
                qty_new = self.books[book.isbn].qty
                if (qty_new < qty_orig) and (tot_qty_new < tot_qty_orig):
                    return True
                else:
                    return False
            elif (1 == qty_orig) and (1 == tot_qty_orig):
                self.books.pop(book.isbn)
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
        if self.book_in_exists(book):
            qty_orig = self.books[book.isbn].qty
            if 0 < qty_orig:
                self.books[book.isbn].qty -= 1
                if self.book_out_exists(book):
                    self.books_out[book.isbn].qty += 1
                else:
                    book_copy = deepcopy(book)
                    book_copy.qty = 1
                    self.books_out[book.isbn] = book_copy
                return True
            elif 0 == qty_orig:
                return False
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
            if self.book_in_exists(book):
                if 1 < qty_orig:
                    self.books_out[book.isbn].qty -= 1
                else:
                    self.books_out.pop(book.isbn)
                self.books[book.isbn].qty += 1
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
            self.patrons.pop(patron.card_num)
            return True
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
        print('6 -- Update a hold on a book')
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


    def print_type_menu(self):
        """Prints the patron or educator type menu to the console"""
        print('Please select one of the following options:')
        print('1 -- Add regular patron')
        print('2 -- Add educator')
        print('x -- Quit')


    def patron_create_prompt(self):
        """Gives prompts to enter patron information and handles user input
        
        Args:
            None
        
        Returns:
            data: a 7-tuple with the following elements
                [0]: num - library card number
                [1]: last - Patron's last name
                [2]: first - Patron's first name
                [3]: dob - Patron's date of birth
                [4]: phone - Patron's phone number
                [5]: email - Patron's email address
                [6]: address - Patron's residential address
        """
        print('Please enter the following information')
        num = input('Library card number: ')
        last = input('Patron\'s last name: ')
        first = input('Patron\'s first name: ')
        dob = input('Patron\'s date of birth (YYYMMDD): ')
        phone = input('Patron\'s phone number: ')
        email = input('Patron\'s email address: ')
        address = input('Patron\'s residential address: ')
        data = (num, last, first, dob, phone, email, address)
        return data


    def ed_hold_prompt(self):
        """Gives prompt to enter hold information and handles user input
        
        Args:
            None
        
        Returns:
            dates: a 2-tuple with the following elements
                [0]: start - hold start date as a string
                [1]: end - hold end date as a string
        """
        print('Please enter the following information')
        start = input('Start date (YYYYMMDD): ')
        end = input('End date (YYYYMMDD): ')
        dates = (start, end)
        return dates


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