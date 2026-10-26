# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Shared text fixtures to provide reusable test data


import pytest
from Mui_Book import Book
from Mui_Patron import Patron, Educator


@pytest.fixture
def sample_book_many():
    """Returns a fully populated Book with realistic data and large quantity"""
    return Book(
        isbn = '9780141439518',
        author = 'Jane Austen',
        title = 'Pride and Prejudice',
        qty = 15
    )


@pytest.fixture
def sample_book_single():
    """Returns a fully populated Book with realistic data with single copy"""
    return Book(
        isbn = '9780140177398',
        author = 'John Steinbeck',
        title = 'Of Mice and Men',
        qty = 1
    )


@pytest.fixture
def sample_book_default():
    """Returns a Book using only required parameters"""
    return Book(
        isbn = '123456789'
    )


@pytest.fixture
def sample_book_dict():
    """Returns a sample dictionary of 11 books"""
    book1 = Book('9780060853983', 'Terry Pratchett & Neil Gaiman', 
                 'Good Omens', 1)
    book2 = Book('9780062073488', 'Agatha Christie', 
                 'And Then There Were None', 1)
    book3 = Book('9780062094889', 'Laura Ingalls Wilder', 
                 'Little House on the Prairie', 1)
    book4 = Book('9780316769174', 'J.D. Slinger', 'The Catcher in the Rye', 1)
    book5 = Book('9780141191508', 'Gaston Leroux', 
                 'The Phantom of the Opera', 1)
    book6 = Book('9780141392608', 'Victor Hugo', 'Les Miserables', 1)
    book7 = Book('9780141439471', 'Mary Shelley', 'Frankenstein', 1)
    book8 = Book('9780142410318', 'Roald Dahl', 
                 'Charlie and the Chocolate Factory', 1)
    book9 = Book('9780141439556', 'Emily Bronte', 'Wuthering Heights', 1)
    book10 = Book('9780141439570', 'Oscar Wilde', 
                  'The Picture of Dorian Gray', 1)
    book11 = Book('9780141439600', 'Charles Dickens', 'A Tale of Two Cities', 1)
    book_dict = {
        book1.isbn: book1,
        book2.isbn: book2,
        book3.isbn: book3,
        book4.isbn: book4,
        book5.isbn: book5,
        book6.isbn: book6,
        book7.isbn: book7,
        book8.isbn: book8,
        book9.isbn: book9,
        book10.isbn: book10,
        book11.isbn: book11,
    }
    return book_dict


@pytest.fixture
def sample_patron():
    """Returns a Patron fully populated with realistic data"""
    return Patron(
        num = '899261678',
        last = 'Deckow',
        first = 'Sonia',
        dob = '19711012',
        phone = '810-932-7365',
        email = 'soniadeckow@protonmail.com',
        address = '9740 Larissa Expressway Apt. 320, Bernitaport, South Dakota, 07123'
    )


@pytest.fixture
def sample_patron_default():
    """Returns a Patron using only required parameters"""
    return Patron(
        num = '111222333'
    )


@pytest.fixture
def sample_educator():
    """Returns an Educator fully populated with realistic data"""
    return Educator(
        num = '888120722',
        last = 'Barrows',
        first = 'Americo',
        dob = '19881015',
        phone = '580-438-9671',
        email = 'americo.barrows68@outlook.com',
        address = '5677 Witting Rest Suite 120, East Harmony, California, 66444',
        institution = 'P.S. 112'
    )


@pytest.fixture
def sample_ed_default():
    """Returns an Educator using only required parameters"""
    return Educator(
        num = '444555666'
    )