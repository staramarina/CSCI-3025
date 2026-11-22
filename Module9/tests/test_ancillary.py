# Tiffany M. Mui
# Module 9 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for ancillary module
# Run with: python -m unittest tests.test_ancillary -v


import unittest
import sys
from pathlib import Path


# Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


import Mui_Ancillary as aux


class TestIntCheck(unittest.TestCase):
    """Class to test the int_check(num_str) function"""

    def test_valid_num(self):
        """Tests various valid integers"""
        num_str1 = '0'
        num_str2 = '27'
        num1 = aux.int_check(num_str1)
        num2 = aux.int_check(num_str2)
        self.assertTrue(num1[0])
        self.assertTrue(0 == num1[1])
        self.assertTrue(num2[0])
        self.assertTrue(27 == num2[1])

    def test_null_input(self):
        """Tests function with missing input"""
        num_str = None
        num = aux.int_check(num_str)
        self.assertFalse(num[0])
        self.assertIn("Invalid input", num[1])

    def test_char_input(self):
        """Tests function with character/string input"""
        num_str1 = 'c'
        num_str2 = 'string'
        num1 = aux.int_check(num_str1)
        num2 = aux.int_check(num_str2)
        self.assertFalse(num1[0])
        self.assertIn("Invalid input", num1[1])
        self.assertFalse(num2[0])
        self.assertIn("Invalid input", num2[1])

    def test_decimal_input(self):
        """Tests function with decimal number input"""
        num_str = '123.45'
        num = aux.int_check(num_str)
        self.assertFalse(num[0])
        self.assertIn("Invalid input", num[1])


if __name__ == "__main__":
    unittest.main()