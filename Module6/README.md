# Tiffany Mui - Module 6 Assignment

A library tool that tracks books and patrons and allows patrons to checkout and return books.

Estimated Minimum: TBD  
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
- (TBD --mechanism of input data)
- (TBD --input data verification)
- (TBD --describe the flow of the main program)

## Features
- **Book Checkout, Return, and Extend** - Allows patrons to checkout and return books as well as extend the due date of a borrowed book
- **Ordered Wait Listing** - If all copies of a book are checked out a patron can request to be placed on a wait list, which prevents borrow extensions
- **Separate Patron and Educator Accounts** - Increases borrow times and item limitations for educators
- **Book Holds** - Allows educators to place holds on books for a future period of time

## Installation

### Prerequisites
- Python 3.6 or higher (estimated) --TBR
- No external dependencies: required modules are either included or use built-in packages. -- TBR

### Setup Steps
1. Download the repository from https://github.com/staramarina/CSCI-3025/tree/main/Module6
2. Verify all files are present
```
   Module6/
    ├── Mui_M6Assignment.py   # Main program
    ├── Mui_Library.py        # Library class module
    ├── Mui_Book.py           # Book class module
    ├── Mui_Patron.py         # Patron class module
    └── TBR
```
3. Ensure Python path includes the Module6 directory or run from within it.

## Usage

### Running the Program
From the Module6 directory  
```python Mui_M6Assignment.py```

### Example Interaction
```
TBD
```

## Project Structure
```
   Module6/
    ├── Mui_M6Assignment.py   # Main program
    ├── Mui_Library.py        # Library class module
    ├── Mui_Book.py           # Book class module
    ├── Mui_Patron.py         # Patron class module
    ├── TBD
    └── README.md             # Read me file (current file)
```

## Modules

### Built-in Packages
- TBD

### Library Module (Mui_Library.py)

#### Library Class
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
| add_book(self, book) | Adds a Book instance to the library inventory | True if book successfully added, otherwise False |
| remove_book(self, book) | Removes a single Book instance from the library altogether | True if book removed successfully, otherwise False |
| decirc_book(self, book) | Remove a book from the circulation inventory and add it to the out of circulation inventory | True if book was successfully moved to decirculation inventory, otherwise False |
| recirc_book(self, book) | Adds a book back into the circulation inventory from the decirculation inventory | True if book successfully moved to circulation inventory, otherwise False |
| patron_exists(self, patron) | Checks whether a patron exists in the library database | True if patron exists, otherwise False |
| add_patron(self, patron) | Adds a Patron instance to the library | False if patron already exists, otherwise True |
| remove_patron(self, patron) | Removes a Patron instance from the library | True if patron exists, otherwise False |
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
| isbn | ISBN of the book | '0' |
| author | Author of the book with first name first | '' |
| title | Title of the book | '' |
| qty | Number of copies the library has available | 1 |
| return_date | Date the book is due to return | None |
| hold_start | Date the hold on a book starts | None |
| hold_end | Date the hold on a book ends | None |
| waitlist | List of library card numbers of patrons waiting for the book | Empty |

##### Methods
| Method | Purpose | Return |
| -------- | -------- | -------- |
| __init__(self, isbn = '0', author = '', title = '', qty = 1) | Initializes as instance of the Book class | book instance |
| show_info(self) | Provides ISBN, author, title, and quantity information for a book | book information as a string |
| show_status(self) | Provides ISBN, author, title, and return date information for a book | book status information as a string |
| show_hold(self) | Provides ISBN, author, title, hold_start, and hold_end information for a book | book hold information as a string |
| book_avail(self) | Determines whether a book is available for checkout (Seems duplicated, TBR) | TBD |
| change_quant(self) | Changes the quantity of books that the library has available (Seems duplicated, TBR) | TBD |

### Patron Module (Mui_Patron.py)

#### Patron Class
Provides information on and support actions of patrons

##### Attributes
| Attribute | Purpose | Default Value |
| -------- | -------- | -------- |
| card_num | Unique library card number | '0' |
| last_name | Patron's last name | '' |
| first_name | Patron's first name | '' |
| dob | Patron's date of birth | '' |
| phone | Patron's phone number | '' |
| email | Patron's email address | '' |
| address | Patron's residential address | '' |
| standing | Patron's standing; good or overdue | 'good' |
| books | List of books the Patron has currently checked out | Empty |

##### Methods
| Method | Purpose | Return |
| -------- | -------- | -------- |
| __init__(self, num = '0', last = '', first = '', dob = None, phone = '', email = '', address = '') | Initializes as instance of the Patron class | patron instance |
| checkout_book(self, book) | Checks out a book to a patron (maybe move to library instead, TBR) | TBD |
| return_book(self, book) | Returns a book back to the library (maybe move to library instead, TBR) | TBD |
| checkout_extend(self, book) | Extends the return date of a book | True if patron has book, otherwise False |
| waitlist_add(self, book) | Adds a patron to the wait list for a book (maybe move to library instead, TBR) | TBD |
| display_checkout(self) | Provides status information on books the patron has checked out | TBD |

#### Educator Subclass (Patron is parent class)
Provides information on and support actions of educators

##### Attributes
| Attribute | Purpose | Default Value |
| -------- | -------- | -------- |
| institution | The educator's institution | TBD |
| hold_books | List of books the educator has requested a hold on | TBD |

##### Methods
| Method | Purpose | Return |
| -------- | -------- | -------- |
| __init__(TBD) | Initializes as instance of the Educator class | educator |
| checkout_book(self, book) | Checks out a book to an educator | TBD |
| checkout_extend(self, book) | Extends the return date of a book | TBD |
| hold_request(self, book) | Places a hold on the requested book | TBD |
| hold_extend(self, book) | Extends the hold on the requested book | TBD |
| hold_remove(self, book) | Removes the hold on the specified book | TBD |

## Input File Format
TBD

### Valid Values
TBD

### Example Input File (TBD.txt)
```
TBD
```

### Verification Rules
TBD

## Testing

### Manual Testing
Run the program with provided test data:  
```python TBD.py```  
Enter: ```TBD```  
Enter: ```TBD```

### Automated Testing
Automated tested with pytest. --TBR


## Author & Credits
Author: Tiffany M. Mui  
Institution: State University of New York: Empire State University  
Course: CSCI-3025 - Python Programming  
Instructor: Dr. Sahand Ziabari  
Date: XX Oct 2026  
