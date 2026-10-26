# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for Mui_Ancillary.py module
# Note: file_exists function tested in Module 5
# Run with: pytest tests/test_ancillary.py -v


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