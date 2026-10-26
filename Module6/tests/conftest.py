# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Shared text fixtures to provide reusable test data


import pytest
import sys
from pathlib import Path


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))
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
def sampe_patron_default():
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
        insitution = 'P.S. 112'
    )


@pytest.fixture
def sample_ed_default():
    """Returns an Educator using only required parameters"""
    return Educator(
        num = '444555666'
    )