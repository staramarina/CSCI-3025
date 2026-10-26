# Tiffany Mui - Module 6 Assignment

A library tool that tracks books and patrons and allows patrons to checkout and return books.

Estimated Minimum: ![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)    
Development Environment: Python 3.14.4

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modules](#modules)
- [Input File Format](#input-file-format)
- [Testing](#testing)
- [Author/Credits](#author--credits)

---

## Overview
The library tool was created for State University of New York (SUNY): Empire State University (ESU), CSCI-3025: Python Programming course as the Module 6 assignment.

The library tool: 
- Instantiates a library instance using example starting data
- Offers separate menus for library staff, patrons, and general book searches
- Staff abilities include adding, decirculating, recirculating, and removing books as well as adding and removing patrons
- Patron abilities include checking out, extending, and returning as well as adding themselves to waitlists for books.
- Educators have the same abilities as patrons, but can also request, update, and remove holds on books
- Searching includes by ISBN, author, or title as well as the ability to display all books in the library

Ground work for the following features is included, but not fully implemented:
- Tracking a patron's status and blocking addition check outs if the account is overdue
- Age-based account types using patron date of birth
- Eligibility restrictions based on patron residential address
- Separation of staff and patron actions is complete, but no authentication is included
- Currently only one educator can place a hold on a book, but ground work is done to allow for changing this in the future

## Features
- **Book Checkout, Return, and Extend** - Allows patrons to checkout and return books as well as extend the due date of a borrowed book
- **Ordered Wait Listing** - If all copies of a book are checked out a patron can request to be placed on a wait list, which prevents borrow extensions
- **Separate Patron and Educator Accounts** - Increases borrow times and item limitations for educators
- **Book Holds** - Allows educators to place holds on books for a future period of time

## Installation

### Prerequisites
- Python 3.10 or higher (estimated)
- No external dependencies: required modules are either included or use built-in packages.

### Setup Steps
1. Download the repository from https://github.com/staramarina/CSCI-3025/tree/main/Module6
2. Verify all files are present
```
   Module6/
    ├── Mui_Ancillary.py         # Ancillary functions module
    ├── Mui_Book.py              # Book class module
    ├── Mui_Library.py           # Library class module
    ├── Mui_M6Assignment.py      # Main program
    ├── Mui_Patron.py            # Patron class module
    ├── testbookdata.txt         # Book data to instantiate a library instance
    ├── testeducatordata.txt     # Educator data to instantiate a library instance
    └── testpatrondata.txt       # Patron data to instantiate a library instance
```
3. Ensure Python path includes the Module6 directory or run from within it.

## Usage

### Running the Program
From the Module6 directory  
```python Mui_M6Assignment.py```

### Example Interaction
```

Mui Mini Library
719-542-7279
123 S Academy Blvd, Fountain, CO 80819


Please select one of the following options:
1 -- Staff Login
2 -- Card Holder Login
3 -- Search Library Database
x -- Quit
2

Please enter your library card number
888120722

Please select one of the following options:
1 -- Checkout a book
2 -- Return a book
3 -- Extend return due date on a book
4 -- Get added to the waitlist for a book
5 -- Request a hold on a book
6 -- Update a hold on a book
7 -- Remove a hold on a book
8 -- View al checked out books
x -- Quit
1

Please enter the ISBN of the book you would like to checkout
9780060853983
Book was successfully checked out
```

## Project Structure
```
   Module6/
    ├── Mui_Ancillary.py         # Ancillary functions module
    ├── Mui_Book.py              # Book class module
    ├── Mui_Library.py           # Library class module
    ├── Mui_M6Assignment.py      # Main program
    ├── Mui_Patron.py            # Patron class module
    ├── README.md                # Read me file (current file)
    ├── pyproject.toml           # Configuration file
    ├── testbookdata.txt         # Book data to instantiate a library instance
    ├── testeducatordata.txt     # Educator data to instantiate a library instance
    ├── testpatrondata.txt       # Patron data to instantiate a library instance
    └── tests/                   # Test files for pytest
          ├── __init__.py        # Tells Python this is a package
          ├── conftest.py        # Shared test fixtures
          ├── test_ancillary.py  # Tests for Mui_Ancillary.py
          ├── test_book.py       # Tests for Mui_Book.py
          ├── test_library.py    # Tests for Mui_Library.py
          └── test_patron.py     # Tests for Mui_Patron.py
```

## Modules

### Built-in Packages
- sys for graceful program exits
- datetime for representing dates and performing date calculations
- copy to make deep copies of instances

### Library Module (Mui_Library.py)

#### Library Class -- TBR
Provides library book inventory and patron management.

##### Attributes
| Attribute | Purpose | Default Value |
| -------- | -------- | -------- |
| name | Name of the library | 'Library' |
| phone | Phone number to call the library | None |
| address | Address to visit the library | None |
| books | Dictionary to hold instances of Book | Empty |
| books_out | Dictionary to hold books that have been pulled from circulation | Empty |
| patrons | Dictionary to hold instances of Patron | Empty |

##### Methods
| Method | Purpose | Return |
| -------- | -------- | -------- |
| __init__(self, name = 'Library', phone = None, address = None) | Initializes an instance of the Library class | library instance |
| book_in_exists(self, book) | Checks whether a book exists in the circulation inventory | True if book exists, otherwise False |
| book_out_exists(self, book) | Checks whether a book exists in the non-circulation inventory | True if book exists, otherwise False |
| find_book(self, isbn) | Finds and turns a book with the specified ISBN | book |
| add_book(self, book) | Adds a Book instance to the library inventory | True if book successfully added, otherwise False |
| remove_book(self, book) | Removes a single Book instance from the library altogether | True if book removed successfully, otherwise False |
| decirc_book(self, book) | Remove a book from the circulation inventory and add it to the out of circulation inventory | True if book was successfully moved to decirculation inventory, otherwise False |
| recirc_book(self, book) | Adds a book back into the circulation inventory from the decirculation inventory | True if book successfully moved to circulation inventory, otherwise False |
| book_avail(self, book) | Determines whether a book is available for checkout | True if quantity in library is at least one, otherwise False |
| find_patron(self, card) | Finds a patron record from their library card number | patron |
| patron_exists(self, patron) | Checks whether a patron exists in the library database | True if patron exists, otherwise False |
| add_patron(self, patron) | Adds a Patron instance to the library | False if patron already exists, otherwise True |
| remove_patron(self, patron) | Removes a Patron instance from the library | True if patron exists, otherwise False |
| menu_bound_check(self, select = 0, type = 0) | Checks whether the selection from the menu is within bounds | True if within bounds, otherwise False |
| print_main_menu(self) | Prints the library main menu to the console | None (Output to console) |
| print_staff_menu(self) | Prints the library staff menu to the console | None (Output to console) |
| print_patron_menu(self) | Prints the patron menu to the console | None (Output to console) |
| print_search_menu(self) | Prints the search menu to the console | None (Output to console) |
| print_type_menu(self) | Prints the patron or educator type menu to the console | None (Output to console) |
| patron_create_prompt | Gives prompts to enter patron information and handles user input | data as a 7-tuple with all input for patron initialization |
| ed_hold_prompt(self) | Gives prompt to enter hold information and handles user input | data as a 3-tuple including start date, end date, and quantity |
| __str__(self) | Provides library name, phone number, and address information | String default output |
| show_books(self) | Prints all books in the library to the console | None (Output to console) |
| search_isbn(self, search) | Prints book information for the given ISBN if it exists | None (Output to console) |
| search_author(self, search) | Prints book information written by given author if they exist | None (Output to console) |
| search_title(self, search) | Prints book information with given title if they exist | None (Output to console) |

### Book Module (Mui_Book.py)

#### Book Class
Provides information and checks on books

##### Attributes
| Attribute | Purpose | Default Value |
| -------- | -------- | -------- |
| isbn | ISBN of the book | N/A |
| author | Author of the book with first name first | '' |
| title | Title of the book | '' |
| qty | Number of copies the library has available | 1 |
| return_date | Date the book is due to return | None |
| hold_start | Date the hold on a book starts | None |
| hold_end | Date the hold on a book ends | None |
| hold_qty | Quantity of books that are on hold | 0 |
| tot_qty | Total quantity of books the library has | 1 |
| waitlist | List of library card numbers of patrons waiting for the book | Empty |

##### Methods
| Method | Purpose | Return |
| -------- | -------- | -------- |
| __init__(self, isbn = '0', author = '', title = '', qty = 1) | Initializes as instance of the Book class | book instance |
| (@property) qty(self) | Used for validated access to book's quantity attribute | self.__qty |
| (@property) tot_qty(self) | Used for validated access to book's total quantity attribute | self.__tot_qty |
| _val_qty(self, value) | Checks quantity value, rejects invalid values | value if no error raised |
| (@qty.setter) qty(self, value) | Sets quantity after validation | self.__qty |
| (@tot_qty.setter) tot_qty(self, value) | Sets quantity after validation | self.__tot_qty |
| hold_check(self) | Checks whether a book is currently within the hold period | True if book is on hold, otherwise False |
| __str__(self) | Provides ISBN, author, title, and quantity information for a book | book information as a string |
| show_status(self) | Provides ISBN, author, title, and return date information for a book | book status information as a string |
| show_hold(self) | Provides ISBN, author, title, hold_start, and hold_end information for a book | book hold information as a string |

### Patron Module (Mui_Patron.py)

#### Patron Class
Provides information on and support actions of patrons

##### Attributes
| Attribute | Purpose | Default Value |
| -------- | -------- | -------- |
| card_num | Unique library card number | N/A |
| last_name | Patron's last name | '' |
| first_name | Patron's first name | '' |
| dob | Patron's date of birth (encapsulated) | '' |
| phone | Patron's phone number (encapsulated) | '' |
| email | Patron's email address (encapsulated) | '' |
| address | Patron's residential address (encapsulated) | '' |
| standing | Patron's standing; good or overdue | 'good' |
| books | List of books the Patron has currently checked out | Empty |

##### Methods
| Method | Purpose | Return |
| -------- | -------- | -------- |
| __init__(self, num = '0', last = '', first = '', dob = None, phone = '', email = '', address = '') | Initializes as instance of the Patron class | patron instance |
| (@property) dob(self) | Validated access to patron's date of birth attribute | self.__dob |
| (@dob.setter) dob(self, value) | Used to valid patron's date of birth | self.__dob |
| (@property) phone(self) | Validated access to patron's phone number attribute | self.__phone |
| (@property) email(self) | Validated access to patron's email address attribute | self.__email |
| (@property) address(self) | Validated access to patron's residential address attribute | self.__address |
| __str__(self) | Provides library card number, last name, and first name | String default output |
| book_check(self, book) | Checks whether a patron has already checked out a book | True if patron has book, otherwise False |
| checkout_book(self, book) | Checks out a book to a patron | (True, success message) if checkout was successful, otherwise (False, error message) |
| return_book(self, book) | Returns a book back to the library | (True, success message) if return was successful, otherwise (False, error message) |
| checkout_extend(self, book) | Extends the return date of a book | (True, success message) if extension was successful, otherwise (False, error message) |
| waitlist_add(self, book) | Adds a patron to the waitlist for a book | patron's index in the waitlist |
| checked_out(self) | Displays information on all books patron has checked out | None (output to Console) |

#### Educator Subclass (Patron is parent class)
Provides information on and support actions of educators

##### Attributes
| Attribute | Purpose | Default Value |
| -------- | -------- | -------- |
| card_num | Unique library card number (Inherited) | N/A |
| last_name | Educator's last name (Inherited) | '' |
| first_name | Educator's first name (Inherited) | '' |
| dob | Educator's date of birth (encapsulated) (Inherited) | '' |
| phone | Educator's phone number (encapsulated) (Inherited) | '' |
| email | Educator's email address (encapsulated) (Inherited) | '' |
| address | Educator's residential address (encapsulated) (Inherited) | '' |
| institution | The educator's institution | '' |
| standing | Educator's standing; good or overdue (Inherited) | 'good' |
| books | List of books the Educator has currently checked out (Inherited) | Empty |
| hold_books | List of books the educator has requested a hold on | Empty |

##### Methods
| Method | Purpose | Return |
| -------- | -------- | -------- |
| __init__(self, num = '0', last = '', first = '', dob = None, phone = '', email = '', address = '', institution = '') | Initializes as instance of the Educator class | educator |
| hold_check(self, book) | Checks whether the educator currently has a hold on the book | (True, qty) if book is on hold and within window, otherwise (False, error message) |
| checkout_book(self, book) | Checks out a book to an educator | (True, success message) if checkout was successful, otherwise (False, error message) |
| checkout_extend(self, book) | Extends the return date of a book | (True, success message) if extension was successful, otherwise (False, error message) |
| hold_request(self, book, start, end, qty) | Places a hold on the requested book | (True, success message) if hold was successful, otherwise (False, error message) |
| hold_update(self, book, start, end, qty) | Updates the hold dates on the requested book | (True, success message) if update was successful, otherwise (False, error message) |
| hold_remove(self, book) | Removes the hold on the specified book | (True, success message) if removal was successful, otherwise (False, error message) |

### Ancillary Module (Mui_Ancillary.py)
Provides additional functions and checks

| Function | Purpose | Return |
| -------- | -------- | -------- |
| file_exists(file_name) | Checks if a file can be opened and read (duplicated function from Module5) | (True, success message) if successful, otherwise (False, error message) |
| int_check(num_str) | Determines whether a string can be converted to an integer | (True, int) if successful, otherwise (False, error message) |
| date_format(date_str) | Formats a string into a datetime | (datetime value, None) if successful, otherwise (None, error message) |

## Input Files
The following files are used to populate a new library instance with example data. Further interaction is intended to occur via the console. Verification rules are the same for both unless otherwise noted. The file names are currently hard-coded, but all such variables are defined immediately following the instantiation of main in the Mui_M6Assignment.py file. 

### Book Data

#### Example Input File (testbookdata.txt)
```
9780140177398, John Steinbeck, Of Mice and Men, 1
9780141191508, Gaston Leroux, The Phantom of the Opera, 2
9780141392608, Victor Hugo, Les Miserables, 5
```

#### Verification Rules
- File input only: A total of 4 values is required
- First value is ISBN and must be unique
- Last value is quantity and must be an integer
- File input only: separate is done via commas, so titles and authors cannot have commas present

### Patron Data

#### Example Input File (testpatrondata.txt)
```
899261678, Deckow, Sonia, 19711012, 810-932-7365, soniadeckow@protonmail.com, 9740 Larissa Expressway Apt. 320, Bernitaport, South Dakota, 07123
118164312, Ruecker, Myles, 19821031, 667-377-2882, mylesruecker@outlook.com, 442 Cayla Lakes, North Maia, West Virginia, 04197
684429935, Windler, Kayley, 19961104. 669-404-2845, kayley.windler@hotmail.com, 900 Joannie Mill, New Gayfort, New Mexico, 07780
```

#### Verification Rules
- File input only: A total of 10 values is required
- First value is the library card number and must be unique
- Fourth value is date of birth and must be in the format YYYYMMDD
- File input only: separation is done via commas, individual values cannot have commas present
- Address components are combined into a single value

### Educator Data

#### Example Input File (testeducatordata.txt)
```
888120722, Barrows, Americo, 19881015, 580-438-9671, americo.barrows68@outlook.com, 5677 Witting Rest Suite 120, East Harmony, California, 66444, American River College
764707335, Reichel, Morgan, 19781220, 630-251-6114, morgan.reichel@hotmail.com, 47180 Jenifer Plains Apt. 307, Clairebury, Alabama, 76390, North Highlands High School
360922899, Klocko, Alan, 19680402, 779-608-1590, alan.klocko82@yahoo.com, 635 Harmon Mill Suite 899, Port Dashawn, South Dakota, 95953, Sierra College
```

#### Verification Rules
- File input only: A total of 11 values is required
- First value is the library card number and must be unique
- Fourth value is date of birth and must be in the format YYYYMMDD
- File input only: separation is done via commas, individual values cannot have commas present
- Address components are combined into a single value

## Testing

### Manual Testing
Manual testing was conducted using the aforementioned input files. Valid values from these files were utilized to test successful branches. Fictitious, both valid and invalid, were used to test the remaining branches. Manual testing was conducted as each branch of the project was completed.

### Automated Testing
Automated tested with pytest. 
From within Module6 directory, run
```
python -m pytest
```

#### Test Fixtures (conftest.py)
| Fixture | Purpose |
| ------- | ------- |
| sample_book_many() | Returns a fully populated Book with realistic data and large quantity |
| sample_book_single() | Returns a fully populated Book with realistic data with single copy |
| sample_book_default() | Returns a Book using only required parameters |
| sample_book_dict() | Returns a sample dictionary of 11 books |
| sample_patron() | Returns a Patron fully populated with realistic data |
| sample_patron_default() | Returns a Patron using only required parameters |
| sample_educator() | Returns and Educator fully populated with realistic data |
| sample_ed_default() | Returns an Educator using only required parameters |

#### Helper Functions (utilities.py)
| Function | Purpose | Returns |
| ------- | ------- | ------- |
| offset_date(**kwargs) | Returns a relative date from now to ensure past and future | rel_dtg as a datetime value |

#### Ancillary Tests (test_ancillary.py)
| Class | Method | Purpose |
| ------- | ------- | ------- |
| TestIntCheck |  | Class to test the int_check(num_str) function |
|  | test_valid_num(self) | Tests expected normal input |
|  | test_null_input(self) | Tests function with missing input |
|  | test_char_input(self) | Tests function with character/string input |
|  | test_decimal_input(self) | Tests function with decimal number input |
| TestDateFormat |  | Class to test the date_format(date_str, future) function |
|  | test_none_input(self) | Tests None input |
|  | test_wrong_length(self) | Tests smaller and larger length input |
|  | test_not_number(self) | Tests non-number values |
|  | test_invalid_dates(self) | Tests dates that don't exist |
|  | test_past_date(self) | Tests both past and future date against past requirement |
|  | test_future_date(self) | Tests both past and future date against future requirement |

#### Book Tests (test_book.py)
| Class | Method | Purpose |
| ------- | ------- | ------- |
| TestBookConstructor |  | Class to test the initialization method |
|  | test_default_values(self, sample_book_default) | Tests that default values are populated when args are missing |
|  | test_init_values(self, sample_book_default) | Tests initialization values that are the same for all books |
|  | test_populated_values(self, sample_book_many) | Tests that passed values override defaults |
|  | test_mutability(self, sample_book_many) | Tests that values expected to change can be changed |
|  | test_qty_neg(self, sample_book_default) | Tests that quantity updates with negative number raises error |
|  | test_qty_type(self, sample_book_default) | Tests that quantity updates with wrong type raises error |
|  | test_qty_bool(self, sample_book_default) | Tests that quantity updates with bool raises error |
| TestHoldCheck |  | Class to test the hold_check(self) method |
|  | test_no_hold(self, sample_book_default) | Tests that hold start and end with None result in False |
|  | test_current_hold(self, sample_book_default) | Tests that a book within the hold period returns true |
|  | test_past_hold(self, sample_book_default) | Tests that a past hold period returns False |
|  | test_future_hold(self, sample_book_default) | Tests that a future hold period returns False |
| TestBookStringRepresentations |  | Class to test the __str__, show_status, and show_hold methods |
|  | test_str_format(self, sample_book_many) | Tests that string appears as expected |
|  | test_str_default(self, sample_book_default) | Tests that a book with default values prints as expected |
|  | test_show_status(self, sample_book_single) | Tests that the return string from show_status is as expected |
|  | test_show_hold(self, sample_book_single) | Tests that the return string from show_hold is as expected |

#### Library Tests (test_library.py)
TBD

#### Patron Tests (test_patron.py)
| Class | Method | Purpose |
| ------- | ------- | ------- |
| TestPatronConstructor |  | Class to test the __init__ method |
|  | test_default_values(self, sample_patron_default) | Tests that default values are populated when args are missing |
|  | test_init_values(self, sample_patron_default) | Tests initialization values that are the same for all patrons |
|  | test_populated_values(self, sample_patron) | Tests that passed values override defaults |
| TestPatronString |  | Class to test the __str__ method |
|  | test_str_format(self, sample_patron) | Tests that string appears as expected |
|  | test_str_default(self, sample_patron_default) | Tests that a book with default values prints as expected |
| TestPatronCheckoutBook |  | Class to test the checkout_book(self, book) method |
|  | test_success_checkout(self, sample_patron, sample_book_many) | Tests the successful checkout of a book |
|  | test_duplicate_checkout(self, sample_patron, sample_book_many) | Tests the duplicate checkout branch |
|  | test_checkout_limit(self, sample_patron, sample_book_many, sample_book_single) | Tests reaching the checkout limit |
| TestReturnBook |  | Class to test the return_book(self, book) method |
|  | test_success_return(self, sample_patron, sample_book_many) | Tests successfully returning a book |
|  | test_fail_return(self, sample_patron, sample_book_single) | Tests failing to return a book |
| TestPatronCheckoutExtend |  | Class to test the checkout_extend(self, book) method |
|  | test_hold_fail(self, sample_patron, sample_book_single) | Tests the failure branch due to a hold on the book |
|  | test_hold_pass(self, sample_patron, sample_book_many) | Tests the success branch, hold, but sufficient quantity |
|  | test_wait_fail(self, sample_patron, sample_book_single) | Tests that extending the checkout fails when there is a waitlist |
|  | test_not_checked(self, sample_patron, sample_book_single) | Tests that attempting to return a book not checked out fails |
| TestWaitlistAdd |  | Class to test the waitlist_add(self, book) method |
|  | test_checked_out(self, sample_patron, sample_book_single) | Tests that adding to waitlist for checked out book fails |
|  | test_add_wait(self, sample_patron, sample_book_single) | Tests that a patron is successfully added to the waitlist |
|  | test_wait_already(self, sample_patron, sample_book_single) | Tests that a patron's position in the waitlist is not changed |
| TestEducatorConstructor |  | Class to test the Educator __init__ method |
|  | test_default_values(self, sample_ed_default) | Tests that default values behave as expected with inheritance |
|  | test_real_values(self, sample_educator) | Tests that real values overwrite defaults with inheritance |
| TestCurrentHold |  | Class to test the hold_book(self, book) method |
|  | test_no_holds(self, sample_educator, sample_book_single) | Tests when there is nothing in the hold books list |
|  | test_too_early(self, sample_educator, sample_book_single) | Tests when the hold has not started yet |
|  | test_too_late(self, sample_educator, sample_book_single) | Tests when the hold has expired |
|  | test_not_hold(self, sample_educator, sample_book_single) | Tests when there is a hold book list, but the book isn't on it |
|  | test_hold_active(self, sample_educator, sample_book_single) | Tests when a hold is active |
| TestEdCheckoutBook |  | Class to test the Educator checkout_book(self, book) method |
|  | test_hold_checkout(self, sample_educator, sample_book_single) | Tests when a book is on hold and checkout is successful |
|  | test_not_enough(self, sample_educator, sample_book_many) | Tests when a book is on hold, but there aren't enough |
|  | test_reg_checkout(self, sample_educator, sample_book_many) | Tests when there is a hold, but book_hold check fails |
| TestHoldRequest |  | Class to test the hold_request(self, book, start, end, qty) method |
|  | test_old_hold(self, sample_educator, sample_book_single) | Tests when the book is already on hold |
|  | test_many_hold(self, sample_educator, sample_book_single) | Tests when there aren't enough books for a hold |
|  | test_past_hold(self, sample_educator, sample_book_single) | Tests when a hold is requested for past dates |
|  | test_end_start(self, sample_educator, sample_book_single) | Tests when the start date is after the end date |
|  | test_hold_success(self, sample_educator, sample_book_single) | Tests when a hold is placed successfully |
| TestHoldUpdate |  | Class to test the hold_update(self, book, start, end) method |
|  | test_not_hold(self, sample_educator, sample_book_single) | Tests when the book is not currently on hold |
|  | test_update_success(self, sample_educator, sample_book_single) | Tests when the hold was successfully updated |
| TestHoldCancel |  | Class to test the hold_remove(self, book) method |
|  | test_hold_cancel(self, sample_educator, sample_book_single) | Tests that a hold is successfully cancelled |

## Author & Credits
Author: Tiffany M. Mui  
Institution: State University of New York: Empire State University  
Course: CSCI-3025 - Python Programming  
Instructor: Dr. Sahand Ziabari  
Date: XX Oct 2026  
