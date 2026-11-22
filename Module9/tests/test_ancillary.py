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


class TestIntCheck:
    """Class to test the int_check(num_str) function"""

    def test_valid_num(self):
        """Tests various valid integers"""
        num_str1 = '0'
        num_str2 = '27'
        num_str3 = '513'
        num1 = aux.int_check(num_str1)
        num2 = aux.int_check(num_str2)
        num3 = aux.int_check(num_str3)
        self.assertTrue(num_str1 == num1)
        self.assertTrue(num_str2 == num2)
        self.assertTrue(num_str3 == num3)


if __name__ == "__main__":
    unittest.main()