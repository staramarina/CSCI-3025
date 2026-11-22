# Tiffany M. Mui
# Module 9 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for parser module
# Run with: TBD (using unittest this time)


import unittest
import os
import sys
import tempfile
from pathlib import Path
import pandas as pd


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


import Mui_Parser as parse


class TestBuildDataframe(unittest.TestCase):
    """Class to test the build_dataframe(file_name) function"""

    @classmethod
    def setUpClass(cls):
        """Setup method to create temporary testing files for the class"""
        cls.tmp_dir = tempfile.TemporaryDirectory()
        base = cls.tmp_dir.name
        with open(os.path.join(base, "good_no_lead.csv"), "w") as f:
            f.write("Date,Description,Amount, Balance\n")
            f.write("11/16/2026,INSOMNIA COOKIES,-7.66,1794.98\n")
        with open(os.path.join(base, "good_lead.csv"), "w") as f:
            f.write("Description,,Summary Amt.\n")
            f.write("\n")
            f.write("Date,Description,Amount, Balance\n")
            f.write("11/16/2026,INSOMNIA COOKIES,-7.66,1794.98\n")
        with open(os.path.join(base, "good_no_head.csv"), "w") as f:
            f.write("11/16/2026,INSOMNIA COOKIES,-7.66,1794.98\n")
        with open(os.path.join(base, "empty.csv"), "w") as f:
            f.write("")

    @classmethod
    def tearDownClass(cls):
        """Tear down method to delete temprorary testing directory"""
        cls.tmp_dir.cleanup()

    def setUp(self):
        """Setup method to create temporary testing directory per method"""
        self.base = self.tmp_dir.name

    def test_default_header(self):
        """Tests the case when there is a header and no leading rows"""
        file_name = os.path.join(self.base, "good_no_lead.csv")
        check = parse.build_dataframe(file_name)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)

    def test_lead_rows(self):
        """Tests the case when there is a header and leading rows"""
        file_name = os.path.join(self.base, "good_lead.csv")
        head_info = 1
        check = parse.build_dataframe(file_name)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)

    def test_no_head(self):
        """Tests the case when there is no header or leading rows"""
        file_name = os.path.join(self.base, "good_no_head.csv")
        head_info = None
        check = parse.build_dataframe(file_name)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)

    def test_empty_file(self):
        """Tests the case when the file exists, but it's empty"""
        file_name = os.path.join(self.base, "empty.csv")
        check = parse.build_dataframe(file_name)
        self.assertFalse(check[0])
        self.assertIn("no parsable data", check[1])
