# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for Mui_Book.py module
# Run with: pytest tests/test_book.py -v


from datetime import datetime
import sys
from pathlib import Path
from utilities import offset_date


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))
from Mui_Book import Book


class TestConstructor:
    """Tests __init__ method"""


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
