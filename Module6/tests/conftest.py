# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Shared text fixtures to provide reusable test data


import pytest
from datetime import datetime, timedelta
import sys
from pathlib import Path


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))
from Mui_Book import Book


def offset_date(**kwargs):
    """Returns a relative date from now to ensure past and future
    
    Args:
        **kwargs: any combination accepted by datetime.timedelta
    
    Returns:
        rel_dtg: datetime value that is offset from now
    """
    rel_dtg = datetime.now() + timedelta(**kwargs)
    return rel_dtg


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
