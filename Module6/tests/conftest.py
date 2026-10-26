# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Shared text fixtures to provide reusable test data


import pytest
from Mui_Book import Book
from Mui_Patron import Patron, Educator
from Mui_Library import Library


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


@pytest.fixture
def sample_lib():
    """returns a Library with realistic data"""
    return Library(
        name = 'Mui Mini Library',
        phone = '719-542-7279', # Example only, do not call
        address = '123 S Academy Blvd, Fountain, CO 80819' # Example only
    )


@pytest.fixture
def default_lib_default():
    """returns a Library with default values"""
    return Library()


@pytest.fixture
def samp_pop_lib():
    """Returns a Library with some books and patrons data included"""
    library = Library(
        name = 'Mui Mini Library',
        phone = '719-542-7279', # Example only, do not call
        address = '123 S Academy Blvd, Fountain, CO 80819' # Example only
    )
    books = sample_book_dict()
    for key, value in books:
        library.books[key] = value
    patron1 = Patron('159225523', 'Runolfsdottir, Magali', '19530103', '470-516-4553', 'magali.runolfsdottir92@icloud.com', '5909 Harris Gardens, New Lueville, Delaware, 72591')
    patron2 = Patron('690341793', 'Padberg, Eliezer', '19931106', '458-320-1047', 'e.padberg@protonmail.com', '29792 Enola Summit Apt. 926, Stevieborough, North Dakota, 48039')
    patron3 = Patron('606936289', 'Okuneva, Francis', '19570428', '470-478-0435', 'fokune@hotmail.com', '359 White Mountain Suite 109, East Domenicahaven, Georgia, 60905')
    patron4 = Patron('183490206', 'Langosh, Brook', '20020821', '986-830-6659', 'brookl02@yahoo.com', '637 Yundt Glen Suite 325, West Montanashire, Kentucky, 80882')
    educator1 = Educator('764707335', 'Reichel, Morgan', '19781220', '630-251-6114', 'morgan.reichel@hotmail.com', '47180 Jenifer Plains Apt. 307, Clairebury, Alabama, 76390', 'North Highlands High School')
    educator2 = Educator('360922899', 'Klocko, Alan', '19680402', '779-608-1590', 'alan.klocko82@yahoo.com', '635 Harmon Mill Suite 899, Port Dashawn, South Dakota, 95953', 'Sierra College')
    educator3 = Educator('380554804', 'Halvorson, Marian', '19810615', '479-235-8856', 'marian296@outlook.com', '53918 Serena Brooks Apt. 661, Lake Janiston, Tennessee, 99256', 'Empire State University')
    library.patrons[patron1.card_num] = patron1
    library.patrons[patron2.card_num] = patron2
    library.patrons[patron3.card_num] = patron3
    library.patrons[patron4.card_num] = patron4
    library.patrons[educator1.card_num] = educator1
    library.patrons[educator2.card_num] = educator2
    library.patrons[educator3.card_num] = educator3


"""
'159225523', 'Runolfsdottir, Magali', '19530103', '470-516-4553', 'magali.runolfsdottir92@icloud.com', '5909 Harris Gardens, New Lueville, Delaware, 72591'
'690341793', 'Padberg, Eliezer', '19931106', '458-320-1047', 'e.padberg@protonmail.com', '29792 Enola Summit Apt. 926, Stevieborough, North Dakota, 48039'
'606936289', 'Okuneva, Francis', '19570428', '470-478-0435', 'fokune@hotmail.com', '359 White Mountain Suite 109, East Domenicahaven, Georgia, 60905'
'183490206', 'Langosh, Brook', '20020821', '986-830-6659', 'brookl02@yahoo.com', '637 Yundt Glen Suite 325, West Montanashire, Kentucky, 80882'


'764707335', 'Reichel, Morgan', '19781220', '630-251-6114', 'morgan.reichel@hotmail.com', '47180 Jenifer Plains Apt. 307, Clairebury, Alabama, 76390', 'North Highlands High School'
'360922899', 'Klocko, Alan', '19680402', '779-608-1590', 'alan.klocko82@yahoo.com', '635 Harmon Mill Suite 899, Port Dashawn, South Dakota, 95953', 'Sierra College'
'380554804', 'Halvorson, Marian', '19810615', '479-235-8856', 'marian296@outlook.com', '53918 Serena Brooks Apt. 661, Lake Janiston, Tennessee, 99256', 'Empire State University'
"""