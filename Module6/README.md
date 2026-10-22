# Tiffany Mui - Module 6 Assignment

A library tool that tracks books and patrons, allows patrons to checkout and return books.

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
(describe what the tool is, why it was made, and what it offers)

## Features
(describe the features of the tool)

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
```python TBD.py```

### Example Interaction
```
TBD
```

## Project Structure
```
   Module6/
    └── TBD
```

## Modules

### Built-in Packages
- TBD

### Library Module (Mui_Library.py)

#### Library Class

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
| __init__(TBD) | Initializes as instance of the Library class | library |
| add_book(self, book) | Adds a Book instance to the library | TBD |
| decirc_book(self, book) | Removes a Book instance from the books dictionary and adds to the out_books dictionary | TBD |
| recirc_book(self, book) | Removes a Book instance from the out_books dictionary and adds to the books dictionary | TBD |
| remove_book(self, book) | Removes a Book instance from the library altogether | TBD |
| add_patron(self, patron) | Adds a Patron instance to the library | TBD |
| remove_patron(self, patron) | Removes a Patron instance from the library | TBD |
| show_books(self) | Shows all books in the library | TBD |
| search_isbn(self, isbn) | Shows all books with the given ISBN | TBD |
| search_author(self, author) | Shows all books with the given author | TBD |
| search_title(self, title) | Shows all books with the given title | TBD |

### Book Module (Mui_Book.py)

#### Book Class

##### Attributes
| Attribute | Purpose | Default Value |
| -------- | -------- | -------- |
| isbn | ISBN of the book | '0' |
| author | Author of the book with first name first | '' |
| title | Title of the book | '' |
| quantity | Number of copies the library has available | 1 |
| return_date | Date the book is due to return | None |
| hold_start | Date the hold on a book starts | None |
| hold_end | Date the hold on a book ends | None |
| waitlist | List of library card numbers of patrons waiting for the book | Empty |

##### Methods
| Method | Purpose | Return |
| -------- | -------- | -------- |
| __init__(TBD) | Initializes as instance of the Book class | book |
| show_info(self) | Provides ISBN, author, title, and quantity information for a book | book_info as a string |
| show_status(self) | Provides ISBN, author, title, and return date information for a book | book_status as a string |
| show_hold(self) | Provides ISBN, author, title, hold_start, and hold_end information for a book | book_hold as a string |

### Patron Module (Mui_Patron.py)

#### Patron Class

##### Attributes
| Attribute | Purpose | Default Value |
| -------- | -------- | -------- |
| card_num | Unique library card number | TBD |
| last_name | Patron's last name | TBD |
| first_name | Patron's first name | TBD |
| dob | Patron's date of birth | TBD |
| phone | Patron's phone number | TBD |
| email | Patron's email address | TBD |
| address | Patron's mailing address | TBD |
| standing | Patron's standing; good, overdue, fines | TBD |
| books | List of books the Patron has currently checked out | TBD |

##### Methods
| Method | Purpose | Return |
| -------- | -------- | -------- |
| __init__(TBD) | Initializes as instance of the Patron class | patron |
| checkout_book(self, book) | Checks out a book to a patron | TBD |
| return_book(self, book) | Returns a book back to the library | TBD |
| checkout_extend(self, book) | Extends the return date of a book | TBD |
| waitlist_add(self, book) | Adds a patron to the wait list for a book | TBD |
| display_checkout(self) | Provides status information on books the patron has checked out | TBD |

#### Educator Subclass (Patron is parent class)

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
