# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for Mui_Patron.py module
# Run with: pytest tests/test_patron.py -v


import sys
from pathlib import Path
from datetime import datetime, timedelta

#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tests.utilities import offset_date


class TestPatronConstructor:
    """Class to test the __init__ method"""


    def test_default_values(self, sample_patron_default):
        """Tests that default values are populated when args are missing"""
        assert '111222333' == sample_patron_default.card_num
        assert '' == sample_patron_default.last_name
        assert '' == sample_patron_default.first_name
        assert None == sample_patron_default.dob
        assert '' == sample_patron_default.phone
        assert '' == sample_patron_default.email
        assert '' == sample_patron_default.address


    def test_init_values(self, sample_patron_default):
        """Tests initialization values that are the same for all patrons"""
        assert 'good' == sample_patron_default.standing
        assert 0 == len(sample_patron_default.books)


    def test_populated_values(self, sample_patron):
        """Tests that passed values override defaults"""
        assert '899261678' == sample_patron.card_num
        assert 'Deckow' == sample_patron.last_name
        assert 'Sonia' == sample_patron.first_name
        assert '19711012' == sample_patron.dob
        assert '810-932-7365' == sample_patron.phone
        assert 'soniadeckow@protonmail.com' == sample_patron.email
        assert '9740 Larissa Expressway Apt. 320, Bernitaport, South Dakota, 07123' == sample_patron.address


class TestPatronString:
    """Class to test the __str__ method"""


    def test_str_format(self, sample_patron):
        """Tests that string appears as expected"""
        expect = ('Card #: 899261678 - Deckow, Sonia')
        assert expect == str(sample_patron)


    def test_str_default(self, sample_patron_default):
        """Tests that a book with default values prints as expected"""
        expect = ('Card #: 111222333 - , ')
        assert expect == str(sample_patron_default)


class TestPatronCheckoutBook:
    """Class to test the checkout_book(self, book) method"""


    def test_success_checkout(self, sample_patron, sample_book_many):
        """Tests the successful checkout of a book"""
        flag = sample_patron.checkout_book(sample_book_many)
        assert flag[0]
        assert sample_book_many.isbn in sample_patron.books
        assert 14 == sample_book_many.qty
        assert 1 == sample_patron.books[sample_book_many.isbn].qty
        assert None != sample_patron.books[sample_book_many.isbn].return_date


    def test_duplicate_checkout(self, sample_patron, sample_book_many):
        """Tests the duplicate checkout branch"""
        flag0 = sample_patron.checkout_book(sample_book_many)
        flag1 = sample_patron.checkout_book(sample_book_many)
        assert flag0[0]
        assert not flag1[0]
        assert 'already checked out' in flag1[1]


    def test_checkout_limit(self, sample_patron, sample_book_many, 
                            sample_book_single):
        """Tests reaching the checkout limit"""
        sample_patron.books = {
            '1': 'Book One',
            '2': 'Book Two',
            '3': 'Book Three',
            '4': 'Book Four',
            '5': 'Book Five',
            '6': 'Book Six',
            '7': 'Book Seven',
            '8': 'Book Eight',
            '9': 'Book Nine',
            '10': 'Book Ten',
            '11': 'Book Eleven'
        }
        flag0 = sample_patron.checkout_book(sample_book_many)
        flag1 = sample_patron.checkout_book(sample_book_single)
        assert flag0[0]
        assert not flag1[0]
        assert 'Cannot exceed checkout limit' in flag1[1]


class TestReturnBook:
    """Class to test the return_book(self, book) method"""


    def test_success_return(self, sample_patron, sample_book_many):
        """Tests successfully returning a book"""
        sample_patron.checkout_book(sample_book_many)
        flag = sample_patron.return_book(sample_book_many)
        assert flag[0]
        assert 15 == sample_book_many.qty
        assert 'successfully returned' in flag[1]


    def test_fail_return(self, sample_patron, sample_book_single):
        """Tests failing to return a book"""
        flag = sample_patron.return_book(sample_book_single)
        assert not flag[0]
        assert 'not checked out' in flag[1]


class TestCheckoutExtend:
    """Class to test the checkout_extend(self, book) method"""


    def test_hold_fail(self, sample_patron, sample_book_single):
        """Tests the failure branch due to a hold on the book"""
        sample_patron.checkout_book(sample_book_single)
        sample_book_single.hold_start = offset_date(days=-5)
        sample_book_single.hold_end = offset_date(days=5)
        flag = sample_patron.checkout_extend(sample_book_single)
        assert not flag[0]
        assert 'Book is on hold' in flag[1]


    def test_hold_pass(self, sample_patron, sample_book_many):
        """Tests the success branch, hold, but sufficient quantity"""
        sample_patron.checkout_book(sample_book_many)
        sample_patron.books[sample_book_many.isbn].return_date = (
                offset_date(weeks=-2))
        orig_return = sample_patron.books[sample_book_many.isbn].return_date
        sample_book_many.hold_start = offset_date(days=-5)
        sample_book_many.hold_end = offset_date(days=5)
        sample_book_many.hold_qty = 5
        flag = sample_patron.checkout_extend(sample_book_many)
        new_return = sample_patron.books[sample_book_many.isbn].return_date
        assert flag[0]
        assert orig_return < new_return
        assert 'successfully extended' in flag[1]


    def test_wait_fail(self, sample_patron, sample_book_single):
        """Tests that extending the checkout fails when there is a waitlist"""
        sample_patron.checkout_book(sample_book_single)
        sample_book_single.waitlist.append('111222333')
        flag = sample_patron.checkout_extend(sample_book_single)
        assert not flag[0]
        assert 'Book is waitlisted' in flag[1]


    def test_not_checked(self, sample_patron, sample_book_single):
        """Tests that attempting to return a book not checked out fails"""
        flag = sample_patron.checkout_extend(sample_book_single)
        assert not flag[0]
        assert 'not currently checked out' in flag[1]