# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for Mui_Ancillary.py module
# Note: file_exists function tested in Module 5
# Run with: pytest tests/test_ancillary.py -v

import sys
from pathlib import Path


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))
import Mui_Ancillary as aux


class TestIntCheck:
    """Class to test the int_check(num_str) function"""


    def test_valid_num(self):
        """Tests expected normal input"""
        num_str1 = '0'
        num_str2 = '27'
        num_str3 = '513'
        num1 = aux.int_check(num_str1)
        num2 = aux.int_check(num_str2)
        num3 = aux.int_check(num_str3)

        assert num1[0]
        assert 0 == num1[1]
        assert num2[0]
        assert 27 == num2[1]
        assert num3[0]
        assert 513 == num3[1]


    def test_null_input(self):
        """Tests function with missing input"""
        num_str = None
        num = aux.int_check(num_str)

        assert not num[0]
        assert 'must be a string' in num[1]


    def test_char_input(self):
        """Tests function with character/string input"""
        num_str1 = 'c'
        num_str2 = 'string'
        num1 = aux.int_check(num_str1)
        num2 = aux.int_check(num_str2)

        assert not num1[0]
        assert 'invalid literal' in num1[1]
        assert not num2[0]
        assert 'invalid literal' in num2[1]


    def test_decimal_input(self):
        """Tests function with decimal number input"""
        num_str = '123.45'
        num = aux.int_check(num_str)

        assert not num[0]
        assert 'invalid literal' in num[1]


class TestDateFormat:
    """Class to test the date_format(date_str) function"""


    def test_none_input(self):
        """Tests None input"""
        date_str = None
        future = False
        dtg = aux.date_format(date_str, future)

        assert dtg[0] is None
        assert 'Date cannot be none' in dtg[1]


    def test_wrong_length(self):
        """Tests smaller and larger length input"""
        future = False
        date_str1 = '199010311'
        date_str2 = '1990103'
        dtg1 = aux.date_format(date_str1, future)
        dtg2 = aux.date_format(date_str2, future)

        assert dtg1[0] is None
        assert 'Incorrect date length' in dtg1[1]
        assert dtg2[0] is None
        assert 'Incorrect date length' in dtg2[1]


    def test_not_number(self):
        """Tests non-number values"""
        future = False
        date_str = 'chardate'
        dtg = aux.date_format(date_str, future)

        assert dtg[0] is None
        assert 'Invalid date formatting' in dtg[1]


    def test_invalid_dates(self):
        """Tests dates that don't exist"""
        future = False
        date_str = '20030229'
        dtg = aux.date_format(date_str, future)

        assert dtg[0] is None
        assert 'Not a valid date' in dtg[1]


    def test_past_date(self):
        """Tests both past and future date against past requirement"""
        future = False
        date_good = '20051031'
        date_bad = '20551031'
        dtg_good = aux.date_format(date_good, future)
        dtg_bad = aux.date_format(date_bad, future)

        assert dtg_good[1] is None
        assert dtg_bad[0] is None
        assert 'Date cannot be in the future' in dtg_bad[1]


    def test_future_date(self):
        """Tests both past and future date against future requirement"""
        future = True
        date_good = '20551031'
        date_bad = '20051031'
        dtg_good = aux.date_format(date_good, future)
        dtg_bad = aux.date_format(date_bad, future)

        assert dtg_good[1] is None
        assert dtg_bad[0] is None
        assert 'Date cannot be in the future' in dtg_bad[1]