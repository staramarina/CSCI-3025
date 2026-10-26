# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for Mui_Patron.py module
# Run with: pytest tests/test_patron.py -v


import sys
from pathlib import Path


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
        assert None == sample_patron_default.__dob
        assert '' == sample_patron_default.__phone
        assert '' == sample_patron_default.__email
        assert '' == sample_patron_default.__address

