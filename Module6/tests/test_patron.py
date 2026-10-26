# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for Mui_Patron.py module
# Run with: pytest tests/test_patron.py -v


import sys
from pathlib import Path
from datetime import datetime

#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))
from Mui_Patron import Patron, Educator


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
