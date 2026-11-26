# Tiffany M. Mui
# Module 9 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for statement class module
# Run with: python -m unittest tests.test_statement -v


import unittest
import sys
from pathlib import Path
import pandas as pd


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


import Mui_Statement as stmnt


class StmntBuild:
    """Class to build various statement class instances for test cases"""

    def build_df6(self):
        """Builds and returns a pandas dataframe with 6 columns"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Post Date": ["", "11/17/2026", "11/16/2026", "11/16/2026"],
            "Amount": [-21.13, -7.66, -28.79, 1500.00],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": [54.12, 12.54, 5.37, 1505.37],
            "Category": ["Restaurants", "Restaurants", "Fast Food", "Income"]
        }
        df = pd.DataFrame(data)
        df["Date"] = pd.to_datetime(df["Date"])
        df["Post Date"] = pd.to_datetime(df["Post Date"])
        df["Amount"] = pd.to_numeric(df["Amount"])
        df["Balance"] = pd.to_numeric(df["Amount"])
        return df

    def build_df4(self):
        """Builds and returns a pandas dataframe with 4 columns"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Amount": [-21.13, -7.66, -28.79, 1500.00],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": [1773.85, 1766.19, 1737.40, 3237.40]
        }
        df = pd.DataFrame(data)
        df["Date"] = pd.to_datetime(df["Date"])
        df["Amount"] = pd.to_numeric(df["Amount"])
        df["Balance"] = pd.to_numeric(df["Amount"])
        return df

    def build_default_stmnt(self):
        """Builds a defaul statement instance"""
        df = self.build_df4()
        return stmnt.Statement(df)

    def build_df6_stmnt(self):
        """Builds a statement instance using the 6 column dataframe"""
        name = "Transactions Test 1.csv"
        df = self.build_df6()
        return stmnt.Statement(df, name)

    def build_df4_stmnt(self):
        """Builds a statement instance using the 4 column dataframe"""
        name = "Transactions Test 2.csv"
        df = self.build_df4()
        return stmnt.Statement(df, name)

    def build_any_stmnt(self, name, df):
        """Returns a statement instance with specified input"""
        return stmnt.Statement(df, name)


class TestStmntMagic(StmntBuild, unittest.TestCase):
    """Class to test the magic functions in the statement class"""

    def setUp(self):
        """Setup method to create test statement class instances"""
        self.stmnt_def = self.build_default_stmnt()
        self.stmnt6 = self.build_df6_stmnt()
        self.stmnt4 = self.build_df4_stmnt()

    def test_default_init(self):
        """Tests the case when name is not supplied on init"""
        self.assertEqual("Transaction Data", self.stmnt_def.name)

    def test_name_override(self):
        """Tests that the name is overridden when specified on init"""
        self.assertEqual("Transactions Test 1.csv", self.stmnt6.name)

    def test_df_pass(self):
        """Tests that a dataframe is successfully added to class instance"""
        self.assertIsInstance(self.stmnt4.df, pd.DataFrame)

    def test_not_dataframe(self):
        """Tests the case when the data variable is not a dataframe on init"""
        not_df = 9
        with self.assertRaises(TypeError) as err:
            self.build_any_stmnt(not_df, "Test")
        self.assertIn("Data must be in a pandas dataframe", str(err.exception))

    def test_add_method(self):
        """Tests tha the __add__ method returns a new combined instance"""
        new_stmnt = self.stmnt4 + self.stmnt6
        self.assertIn("Post Date", new_stmnt.df.columns)
        self.assertEqual(8, len(new_stmnt.df))


if __name__ == "__main__":
    unittest.main()