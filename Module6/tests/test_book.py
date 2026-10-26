# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for Mui_Book.py module
# Run with: pytest tests/test_book.py -v


from datetime import datetime
import pytest
import sys
from pathlib import Path


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))
from Mui_Book import Book
from tests.utilities import offset_date


class TestConstructor:
    """Class to test the __init__ method"""


    def test_default_values(self, sample_book_default):
        """Tests that default values are populated when args are missing"""
        assert '' == sample_book_default.author
        assert '' == sample_book_default.title
        assert 1 == sample_book_default.qty


    def test_init_values(self, sample_book_default):
        """Tests initiatlization values that are the same for all books"""
        assert sample_book_default.return_date is None
        assert sample_book_default.hold_start is None
        assert sample_book_default.hold_end is None
        assert 0 == len(sample_book_default.waitlist)


    def test_populated_values(self, sample_book_many):
        """Tests that passed values override defaults"""
        assert '9780141439518' == sample_book_many.isbn
        assert 'Jane Austen' == sample_book_many.author
        assert 'Pride and Prejudice' == sample_book_many.title
        assert 15 == sample_book_many.qty


    def test_mutability(self, sample_book_many):
        """Tests that values expected to change can be changed"""
        sample_book_many.qty = 21
        sample_book_many.return_date = offset_date(weeks=3)
        assert 21 == sample_book_many.qty
        assert sample_book_many.return_date is not None


    def test_qty_neg(self, sample_book_default):
        """Tests that quantity updates with negative number raises error"""
        qty_neg = -1
        with pytest.raises(ValueError) as exc_info:
            sample_book_default.qty = qty_neg
        assert 'Quantity cannot be negative' == str(exc_info.value)


    def test_qty_type(self, sample_book_default):
        """Tests that quantity updates with wrong type raises error"""
        qty_bad_type = 'char'
        with pytest.raises(TypeError) as exc_info:
            sample_book_default.qty = qty_bad_type
        assert 'Quantity must be an integer' == str(exc_info.value)


    def test_qty_bool(self, sample_book_default):
        """Tests that quantity updates with bool raises error"""
        qty_bool = False
        with pytest.raises(TypeError) as exc_info:
            sample_book_default.qty = qty_bool
        assert 'Quantity must be an integer' == str(exc_info.value)


class TestHoldCheck:
    """Class to test the hold_check(self) method"""


    def test_no_hold(self, sample_book_default):
        """Tests that hold start and end with None result in False"""
        assert sample_book_default.hold_check() is False


    def test_current_hold(self, sample_book_default):
        """Tests that a book within the hold period returns true"""
        sample_book_default.hold_start = offset_date(days=-3)
        sample_book_default.hold_end = offset_date(days=3)
        assert sample_book_default.hold_check() is True


    def test_past_hold(self, sample_book_default):
        """Tests that a past hold period returns False"""
        sample_book_default.hold_start = offset_date(days=3)
        sample_book_default.hold_end = offset_date(days=9)
        assert sample_book_default.hold_check() is False


    def test_future_hold(self, sample_book_default):
        """Tests that a future hold period returns False"""
        sample_book_default.hold_start = offset_date(days=-9)
        sample_book_default.hold_end = offset_date(days=-3)
        assert sample_book_default.hold_check() is False


class TestStringRepresentations:
    """Class to test the __str__, show_status, and show_hold methods"""

    def test_str_format(self, sample_book_many):
        """Tests that string appears as expected"""
        expect = ('ISBN: 9780141439518, Author: Jane Austen, '
                  'Title: Pride and Prejudice, Available Quantity: 15')
        assert expect == str(sample_book_many)


    def test_str_default(self, sample_book_default):
        """Tests that a book with default values prints as expected"""
        expect = ('ISBN: 123456789, Author: , '
                  'Title: , Available Quantity: 1')
        assert expect == str(sample_book_default)


    def test_show_status(self, sample_book_single):
        """Tests that the return string from show_status is as expected"""
        due = offset_date(weeks=3)
        sample_book_single.return_date = due
        expect = ('ISBN: 9780140177398, Author: John Steinbeck, '
                  f'Title: Of Mice and Men, Return Date: {due}')
        assert expect == sample_book_single.show_status()


    def test_show_hold(self, sample_book_single):
        """Tests that the return string from show_hold is as expected"""
        start = offset_date(days=-3)
        end = offset_date(days=9)
        sample_book_single.hold_start = start
        sample_book_single.hold_end = end
        expect = ('ISBN: 9780140177398, Author: John Steinbeck, '
                  'Title: Of Mice and Men, '
                  f'Hold Start: {start}, Hold End: {end}')
        assert expect == sample_book_single.show_hold()