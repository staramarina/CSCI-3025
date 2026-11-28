# Tiffany M. Mui
# Module 9 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for parser module
# Run with: python -m unittest tests.test_parser -v


import unittest
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch
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
        with open(os.path.join(base, "bom_no_head.csv"), "w", 
                  encoding="utf-8-sig") as f:
            f.write("11/16/2026,INSOMNIA COOKIES,-7.66,1794.98\n")
        with open(os.path.join(base, "not_enough.csv"), "w") as f:
            f.write("11/16/2026,-7.66\n")

    @classmethod
    def tearDownClass(cls):
        """Tear down method to delete temporary testing directory"""
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
        self.assertIn("Date", check[1].columns)
        self.assertIn("Amount", check[1].columns)

    def test_lead_rows(self):
        """Tests the case when there is a header and leading rows"""
        file_name = os.path.join(self.base, "good_lead.csv")
        check = parse.build_dataframe(file_name)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertIn("Date", check[1].columns)
        self.assertIn("Amount", check[1].columns)

    def test_no_head(self):
        """Tests the case when there is no header or leading rows"""
        file_name = os.path.join(self.base, "good_no_head.csv")
        check = parse.build_dataframe(file_name)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)

    def test_empty_file(self):
        """Tests the case when the file exists, but it's empty"""
        file_name = os.path.join(self.base, "empty.csv")
        check = parse.build_dataframe(file_name)
        self.assertFalse(check[0])
        self.assertIn("no parsable data", check[1])

    def test_utf8_bom(self):
        """Tests the case when CSV is UTF-8 BOM format"""
        file_name = os.path.join(self.base, "bom_no_head.csv")
        check = parse.build_dataframe(file_name)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)

    def test_few_columns(self):
        """Tests the case of less than 3 columns"""
        file_name = os.path.join(self.base, "not_enough.csv")
        check = parse.build_dataframe(file_name)
        self.assertFalse(check[0])
        self.assertIn("parsing error", check[1])


class TestInferHeader(unittest.TestCase):
    """Class to test the infer_header(data) function"""

    def test_infer_date1(self):
        """Tests the case of a single date column and one money column"""
        data = {
            0: ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            1: ["-21.13", "-7.66", "-28.79", "1500.00"],
            2: ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.infer_header(df)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertIn("Date", check[1].columns)
        self.assertIn("Amount", check[1].columns)

    def test_infer_date2(self):
        """Tests the case of two date columns"""
        data = {
            0: ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            1: ["", "11/17/2026", "11/16/2026", "11/16/2026"],
            2: ["-21.13", "-7.66", "-28.79", "1500.00"],
            3: ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.infer_header(df)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertIn("Date", check[1].columns)
        self.assertIn("Post Date", check[1].columns)

    def test_infer_date3(self):
        """Tests the case of three date columns"""
        data = {
            0: ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            1: ["", "11/17/2026", "11/16/2026", "11/16/2026"],
            2: ["-21.13", "-7.66", "-28.79", "1500.00"],
            3: ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"],
            4: ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"]
        }
        df = pd.DataFrame(data)
        check = parse.infer_header(df)
        self.assertFalse(check[0])
        self.assertIn("Could not verify date", check[1])

    def test_infer_date0(self):
        """Tests the case of no date column"""
        data = {
            0: ["-21.13", "-7.66", "-28.79", "1500.00"],
            1: ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"],
        }
        df = pd.DataFrame(data)
        check = parse.infer_header(df)
        self.assertFalse(check[0])
        self.assertIn("Could not verify date", check[1])

    def test_infer_deb_crd(self):
        """Tests the case of two money columns, debit and credit"""
        data = {
            0: ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            1: ["-21.13", "-7.66", "-28.79", ""],
            2: ["", "", "", "1500.00"],
            3: ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.infer_header(df)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertIn("Debit", check[1].columns)
        self.assertIn("Credit", check[1].columns)

    def test_infer_amt_bal(self):
        """Tests the case of two money columns, amount and balance"""
        data = {
            0: ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            1: ["-21.13", "-7.66", "-28.79", "1500.00"],
            2: ["54.12", "12.54", "5.37", "1505.37"],
            3: ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.infer_header(df)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertIn("Amount", check[1].columns)
        self.assertIn("Balance", check[1].columns)

    def test_infer_mon3(self):
        """Tests the case of three money columns"""
        data = {
            0: ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            1: ["-21.13", "-7.66", "-28.79", ""],
            2: ["", "", "", "1500.00"],
            3: ["54.12", "12.54", "5.37", "1505.37"],
            4: ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.infer_header(df)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertIn("Debit", check[1].columns)
        self.assertIn("Credit", check[1].columns)
        self.assertIn("Balance", check[1].columns)

    def test_infer_mon0(self):
        """Tests the case of no money columns"""
        data = {
            0: ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            1: ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.infer_header(df)
        self.assertFalse(check[0])
        self.assertIn("Could not verify decimal", check[1])


class TestDateFormat(unittest.TestCase):
    """Class to test the date_format(column: pd.Series) function"""

    def test_year_first(self):
        """Tests the case when the year is clearly first part"""
        series = pd.Series([
            "2026-11-18", "2026-11-19", "2026-11-20", 
            "2026-11-21", "2026-11-22", "2026-11-23"
        ], name="Date")
        yr_first, day_first, determine, mixed = parse.date_format(series)
        self.assertTrue(yr_first)
        self.assertFalse(day_first)
        self.assertTrue(determine)
        self.assertFalse(mixed)

    def test_day_first(self):
        """Tests the case when day is clearly first part"""
        series = pd.Series([
            "18-11-2026", "19-11-2026", "20-11-2026", 
            "21-11-2026", "22-11-2026", "23-11-2026"
        ], name="Date")
        yr_first, day_first, determine, mixed = parse.date_format(series)
        self.assertFalse(yr_first)
        self.assertTrue(day_first)
        self.assertTrue(determine)
        self.assertFalse(mixed)

    def test_mon_first(self):
        """Tests the case when day is clearly second part"""
        series = pd.Series([
            "11-18-2026", "11-19-2026", "11-20-2026", 
            "11-21-2026", "11-22-2026", "11-23-2026"
        ], name="Date")
        yr_first, day_first, determine, mixed = parse.date_format(series)
        self.assertFalse(yr_first)
        self.assertFalse(day_first)
        self.assertTrue(determine)
        self.assertFalse(mixed)

    def test_sep_mixed(self):
        """Tests the case when there are mixed separators"""
        series = pd.Series([
            "11-18-2026", "11/19/2026", "11-20-2026", 
            "11-21-2026", "11/22/2026", "11-23-2026"
        ], name="Date")
        yr_first, day_first, determine, mixed = parse.date_format(series)
        self.assertFalse(yr_first)
        self.assertFalse(day_first)
        self.assertTrue(determine)
        self.assertTrue(mixed)

    def test_year_mixed(self):
        """Tests the case when year is last and mixed YYYY and YY"""
        series = pd.Series([
            "11-18-2026", "11-19-26", "11-20-2026", 
            "11-21-2026", "11-22-26", "11-23-2026"
        ], name="Date")
        yr_first, day_first, determine, mixed = parse.date_format(series)
        self.assertFalse(yr_first)
        self.assertFalse(day_first)
        self.assertTrue(determine)
        self.assertTrue(mixed)

    def test_day_mixed(self):
        """Tests the case when there is a mix of date first and second"""
        series = pd.Series([
            "11-18-2026", "19-11-2026", "11-20-2026", 
            "11-21-2026", "22-11-2026", "11-23-2026"
        ], name="Date")
        yr_first, day_first, determine, mixed = parse.date_format(series)
        self.assertFalse(yr_first)
        self.assertFalse(day_first)
        self.assertFalse(determine)
        self.assertTrue(mixed)

    def test_ambiguous(self):
        """Tests the case when day position cannot be determined"""
        series = pd.Series([
            "01-02-03", "02-03-04", "03-04-05", 
            "04-05-03", "05-06-04", "10-11-12"
        ], name="Date")
        yr_first, day_first, determine, mixed = parse.date_format(series)
        self.assertFalse(yr_first)
        self.assertFalse(day_first)
        self.assertFalse(determine)
        self.assertFalse(mixed)


class TestCleanDate(unittest.TestCase):
    """Class to test the date_clean(data, col, yr_first, day_first, determine, 
    mixed) function"""

    def test_yr1_det(self):
        """Tests the case when the year is clearly first part"""
        col = "Date"
        df = pd.DataFrame({ col: [
            "2026-11-18", "2026-11-19", "2026-11-20", 
            "2026-11-21", "2026-11-22", "2026-11-23"
        ]})
        yr1 = True
        day1 = False
        det = True
        mix = False
        check = parse.date_clean(df, col, yr1, day1, det, mix)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertTrue(pd.api.types.is_datetime64_dtype(check[1]["Date"]))

    def test_day1_det(self):
        """Tests the case when day is clearly first part"""
        col = "Date"
        df = pd.DataFrame({ col: [
            "18-11-2026", "19-11-2026", "20-11-2026", 
            "21-11-2026", "22-11-2026", "23-11-2026"
        ]})
        yr1 = False
        day1 = True
        det = True
        mix = False
        check = parse.date_clean(df, col, yr1, day1, det, mix)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertTrue(pd.api.types.is_datetime64_dtype(check[1]["Date"]))

    def test_mon1_det(self):
        """Tests the case when day is clearly second part"""
        col = "Date"
        df = pd.DataFrame({ col: [
            "11-18-2026", "11-19-2026", "11-20-2026", 
            "11-21-2026", "11-22-2026", "11-23-2026"
        ]})
        yr1 = False
        day1 = False
        det = True
        mix = False
        check = parse.date_clean(df, col, yr1, day1, det, mix)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertTrue(pd.api.types.is_datetime64_dtype(check[1]["Date"]))

    def test_det_sep_mix(self):
        """Tests the case when there are mixed separators"""
        col = "Date"
        df = pd.DataFrame({ col: [
            "11-18-2026", "11/19/2026", "11-20-2026", 
            "11-21-2026", "11/22/2026", "11-23-2026"
        ]})
        yr1 = False
        day1 = False
        det = True
        mix = True
        check = parse.date_clean(df, col, yr1, day1, det, mix)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertTrue(pd.api.types.is_datetime64_dtype(check[1]["Date"]))

    def test_det_yr_mix(self):
        """Tests the case when year is last and mixed YYYY and YY"""
        col = "Date"
        df = pd.DataFrame({ col: [
            "11-18-2026", "11-19-26", "11-20-2026", 
            "11-21-2026", "11-22-26", "11-23-2026"
        ]})
        yr1 = False
        day1 = False
        det = True
        mix = True
        check = parse.date_clean(df, col, yr1, day1, det, mix)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertTrue(pd.api.types.is_datetime64_dtype(check[1]["Date"]))

    def test_day1_mix(self):
        """Tests the case when there is a mix of date first and second"""
        col = "Date"
        df = pd.DataFrame({ col: [
            "11-18-2026", "19-11-2026", "11-20-2026", 
            "11-21-2026", "22-11-2026", "11-23-2026"
        ]})
        yr1 = False
        day1 = False
        det = False
        mix = True
        check = parse.date_clean(df, col, yr1, day1, det, mix)
        self.assertFalse(check[0])
        self.assertIn("have mixed format", check[1])

    def test_all_false_pass(self):
        """Tests the case when day position cannot be determined"""
        col = "Date"
        df = pd.DataFrame({ col: [
            "01-02-03", "02-03-04", "03-04-05", 
            "04-05-03", "05-06-04", "10-11-12"
        ]})
        yr1 = False
        day1 = False
        det = False
        mix = False
        with patch("builtins.input", return_value="Y"):
            check = parse.date_clean(df, col, yr1, day1, det, mix)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertTrue(pd.api.types.is_datetime64_dtype(check[1]["Date"]))

    def test_all_false_fail(self):
        """Tests the case when day position cannot be determined"""
        col = "Date"
        df = pd.DataFrame({ col: [
            "01-02-03", "02-03-04", "03-04-05", 
            "04-05-03", "05-06-04", "10-11-12"
        ]})
        yr1 = False
        day1 = False
        det = False
        mix = False
        with patch("builtins.input", return_value="N"):
            check = parse.date_clean(df, col, yr1, day1, det, mix)
        self.assertFalse(check[0])
        self.assertIn("Process aborted", check[1])

    def test_date_convert_fail(self):
        """Tests the case when all date values fail to convert"""
        col = "Date"
        df = pd.DataFrame({ col: [
            "no-date", "missing", "N/A", 
        ]})
        yr1 = False
        day1 = False
        det = True
        mix = False
        check = parse.date_clean(df, col, yr1, day1, det, mix)
        self.assertFalse(check[0])
        self.assertIn("failed to convert", check[1])

class TestCleanMoney(unittest.TestCase):
    """Class to test the clean_money(data, col) function"""

    def test_num_convert(self):
        """Tests that regular numbers are converted to floats"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Post Date": ["", "11/17/2026", "11/16/2026", "11/16/2026"],
            "Amount": [-21.13, "-7.66", 28.79, "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        exp = [-21.13, -7.66, 28.79, 1500.00]
        check = parse.clean_money(df, "Amount")
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        for rx, ex in zip(check[1]["Amount"], exp):
            self.assertAlmostEqual(rx, ex)

    def test_symbol_strip(self):
        """Tests that additional symbols are stripped when converting"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Post Date": ["", "11/17/2026", "11/16/2026", "11/16/2026"],
            "Amount": ["(21.13)", "-7.66", "$28.79", "1,500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        exp = [-21.13, -7.66, 28.79, 1500.00]
        check = parse.clean_money(df, "Amount")
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        for rx, ex in zip(check[1]["Amount"], exp):
            self.assertAlmostEqual(rx, ex)

    def test_invalid_num(self):
        """Tests that full invalid numbers result in error message"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Post Date": ["", "11/17/2026", "11/16/2026", "11/16/2026"],
            "Amount": ["-abc", "", "def", "xyz"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.clean_money(df, "Amount")
        self.assertFalse(check[0])
        self.assertIn("has no values", check[1])

    def test_orig_num(self):
        """Tests that the original data was not modified"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Post Date": ["", "11/17/2026", "11/16/2026", "11/16/2026"],
            "Amount": ["(21.13)", "-7.66", "$28.79", "1,500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        exp = ["(21.13)", "-7.66", "$28.79", "1,500.00"]
        parse.clean_money(df, "Amount")
        for rx, ex in zip(df["Amount"], exp):
            self.assertEqual(rx, ex)

    def test_bal_chg(self):
        """Tests that a mostly negative balance column is updated"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Post Date": ["", "11/17/2026", "11/16/2026", "11/16/2026"],
            "Amount": [-21.13, -7.66, -28.79, 1500.00],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": [-54.12, -12.54, -5.37, -1505.37]
        }
        df = pd.DataFrame(data)
        exp = [54.12, 12.54, 5.37, 1505.37]
        check = parse.clean_money(df, "Balance")
        self.assertTrue(check[0])
        for rx, ex in zip(check[1]["Balance"], exp):
            self.assertEqual(rx, ex)

    def test_amnt_chg(self):
        """Tests that a mostly positive amount column is updated"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Post Date": ["", "11/17/2026", "11/16/2026", "11/16/2026"],
            "Amount": [21.13, 7.66, 28.79, -1500.00],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": [54.12, 12.54, 5.37, 1505.37]
        }
        df = pd.DataFrame(data)
        exp = [-21.13, -7.66, -28.79, 1500.00]
        check = parse.clean_money(df, "Amount")
        self.assertTrue(check[0])
        for rx, ex in zip(check[1]["Amount"], exp):
            self.assertEqual(rx, ex)


class TestMergeDebCrd(unittest.TestCase):
    """Class to test the merge_deb_crd(data) function"""

    def test_keep_sign(self):
        """Tests the case of negative debit and positive credit in original"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Debit": ["-21.13", "-7.66", "-28.79", ""],
            "Credit": ["", "", "", "1500.00"],
            "Description": ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        exp = [-21.13, -7.66, -28.79, 1500.00]
        check = parse.merge_deb_crd(df)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertIn("Amount", check[1].columns)
        self.assertNotIn("Debit", check[1].columns)
        self.assertNotIn("Credit", check[1].columns)
        for rx, ex in zip(check[1]["Amount"], exp):
            self.assertAlmostEqual(rx, ex)


    def test_chg_debit(self):
        """Tests the case when debit is positive"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Debit": ["21.13", "7.66", "28.79", ""],
            "Credit": ["", "", "", "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        exp = [-21.13, -7.66, -28.79, 1500.00]
        check = parse.merge_deb_crd(df)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        for rx, ex in zip(check[1]["Amount"], exp):
            self.assertAlmostEqual(rx, ex)

    def test_chg_credt(self):
        """Tests the case when credit is negative"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Debit": ["-21.13", "-7.66", "-28.79", ""],
            "Credit": ["", "", "", "-1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        exp = [-21.13, -7.66, -28.79, 1500.00]
        check = parse.merge_deb_crd(df)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        for rx, ex in zip(check[1]["Amount"], exp):
            self.assertAlmostEqual(rx, ex)

    def test_deb_crd_conflict(self):
        """Tests the case when there is data in both debit and credit columns"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Debit": ["-21.13", "-7.66", "-28.79", ""],
            "Credit": ["", "14.54", "", "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.merge_deb_crd(df)
        self.assertFalse(check[0])
        self.assertIn("Conflicting debit/credit information", check[1])

    def test_deb_crd_null(self):
        """Tests the case when neither debit nor credit have data"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Debit": ["", "", "", ""],
            "Credit": ["", "", "", ""],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.merge_deb_crd(df)
        self.assertFalse(check[0])
        self.assertIn("Failed to merge columns", check[1])

    def test_deb_crd_orig(self):
        """Tests that the original dataframe still has debit/credit columns"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Debit": ["-21.13", "-7.66", "-28.79", ""],
            "Credit": ["", "", "", "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        parse.merge_deb_crd(df)
        self.assertIn("Debit", df.columns)
        self.assertIn("Credit", df.columns)


class TestCleanDataframe(unittest.TestCase):
    """Class to test the clean_dataframe(data_raw) function"""

    #def setUp(self):
    #    """Setup method to create temporary testing directory"""
    #    self.__tmpdir = tempfile.TemporaryDirectory()
    #    self.err_log = os.path.join(self.__tmpdir.name, "log.txt")

    #def tearDown(self):
    #    """Tear down method to delete temporary testing directory"""
    #    self.__tmpdir.cleanup()

    def test_simple_clean_success(self):
        """Tests that case of Date, Amount, Description, Balance passes"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Amount": ["-21.13", "-7.66", "-28.79", "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": ["1773.85", "1766.19", "1737.40", "3237.40"]
        }
        df = pd.DataFrame(data)
        check = parse.clean_dataframe(df)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertIn("Date", check[1].columns)
        self.assertIn("Amount", check[1].columns)
        self.assertIn("Description", check[1].columns)
        self.assertIn("Balance", check[1].columns)
        self.assertTrue(pd.api.types.is_datetime64_dtype(check[1]["Date"]))
        self.assertTrue(pd.api.types.is_float_dtype(check[1]["Amount"]))
        self.assertTrue(pd.api.types.is_float_dtype(check[1]["Balance"]))

    def test_call_infer_header(self):
        """Tests that the infer_header is called appropriately when forced"""
        data = {
            0: ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            1: ["-21.13", "-7.66", "-28.79", "1500.00"],
            2: ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        with patch("builtins.input", return_value="Y"):
            check = parse.clean_dataframe(df)
        self.assertTrue(check[0])
        self.assertIn("Date", check[1].columns)
        self.assertIn("Amount", check[1].columns)

    def test_header_warn_abort(self):
        """Tests that aborting at the header warning stops processing"""
        data = {
            0: ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            1: ["-21.13", "-7.66", "-28.79", "1500.00"],
            2: ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        with patch("builtins.input", return_value="N"):
            check = parse.clean_dataframe(df)
        self.assertFalse(check[0])
        self.assertIn("Process aborted", check[1])

    def test_multi_date2(self):
        """Tests the case of multiple dates in header rows"""
        data = {
            "Transaction Date": ["11/18/2026", "11/16/2026", 
                                 "11/16/2026", "11/15/2026"],
            "Post Date": ["", "11/17/2026", "11/16/2026", "11/16/2026"],
            "Amount": ["-21.13", "-7.66", "-28.79", "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.clean_dataframe(df)
        self.assertTrue(check[0])
        self.assertIn("Date", check[1].columns)
        self.assertIn("Post Date", check[1].columns)
        self.assertTrue(pd.api.types.is_datetime64_dtype(check[1]["Date"]))
        self.assertTrue(pd.api.types.is_datetime64_dtype(check[1]["Post Date"]))
        self.assertEqual(4, check[1]["Date"].notna().sum())

    def test_multi_date3(self):
        """Tests the case of three date columns"""
        data = {
            "Transaction Date": ["11/18/2026", "11/16/2026", 
                                 "11/16/2026", "11/15/2026"],
            "Effective Date": ["11/18/2026", "11/17/2026", 
                               "11/16/2026", "11/16/2026"],
            "Post Date": ["", "11/17/2026", "11/16/2026", "11/16/2026"],
            "Amount": ["-21.13", "-7.66", "-28.79", "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.clean_dataframe(df)
        self.assertTrue(check[0])
        self.assertIn("Date", check[1].columns)
        self.assertIn("Post Date", check[1].columns)
        self.assertNotIn("Transaction Date", check[1].columns)
        self.assertNotIn("Effective Date", check[1].columns)

    def test_post_date_only(self):
        """Tests the case where post date is the only date column"""
        data = {
            "Post Date": ["11/18/2026", "11/17/2026", 
                          "11/16/2026", "11/16/2026"],
            "Amount": ["-21.13", "-7.66", "-28.79", "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.clean_dataframe(df)
        self.assertTrue(check[0])
        self.assertIn("Date", check[1].columns)
        self.assertNotIn("Post Date", check[1].columns)

    def test_force_ambig_date(self):
        """Tests when ambiguous date assumption is accepted"""
        data = {
            "Date": ["07/01/10", "07/02/10", "07/02/10", "07/03/10"],
            "Amount": ["-21.13", "-7.66", "-28.79", "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": ["1773.85", "1766.19", "1737.40", "3237.40"]
        }
        df = pd.DataFrame(data)
        with patch("builtins.input", return_value="Y"):
            check = parse.clean_dataframe(df)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertTrue(pd.api.types.is_datetime64_dtype(check[1]["Date"]))

    def test_abort_ambig_date(self):
        """Tests when ambiguous date processing is aborted"""
        data = {
            "Date": ["07/01/10", "07/02/10", "07/02/10", "07/03/10"],
            "Amount": ["-21.13", "-7.66", "-28.79", "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": ["1773.85", "1766.19", "1737.40", "3237.40"]
        }
        df = pd.DataFrame(data)
        with patch("builtins.input", return_value="N"):
            check = parse.clean_dataframe(df)
        self.assertFalse(check[0])
        self.assertIn("Process aborted", check[1])

    def test_force_bad_num(self):
        """Tests when number conversion failure is accepted"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Amount": ["-21.13", "-7.66", "-28.79", "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": ["missing", "not here", "N/A", "error"]
        }
        df = pd.DataFrame(data)
        with patch("builtins.input", return_value="Y"):
            check = parse.clean_dataframe(df)
        self.assertTrue(check[0])
        self.assertIn("Amount", check[1].columns)
        self.assertNotIn("Balance", check[1].columns)

    def test_abort_bad_num(self):
        """Tests when number conversion failure is aborted"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Amount": ["-21.13", "-7.66", "-28.79", "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": ["missing", "not here", "N/A", "error"]
        }
        df = pd.DataFrame(data)
        with patch("builtins.input", return_value="N"):
            check = parse.clean_dataframe(df)
        self.assertFalse(check[0])
        self.assertIn("Process aborted", check[1])

    def test_deb_crd_merge(self):
        """Tests that debit/credit columns renamed and merged"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Amount Debit": ["-21.13", "-7.66", "-28.79", ""],
            "Amount Credit": ["", "", "", "1500.00"],
            "Description": ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        exp = [-21.13, -7.66, -28.79, 1500.00]
        check = parse.clean_dataframe(df)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)
        self.assertIn("Amount", check[1].columns)
        self.assertNotIn("Debit", check[1].columns)
        self.assertNotIn("Credit", check[1].columns)
        for rx, ex in zip(check[1]["Amount"], exp):
            self.assertAlmostEqual(rx, ex)

    def test_deb_crd_conflict(self):
        """Tests that debit/credit merge conflicts are integrated"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Debit": ["-21.13", "-7.66", "-28.79", ""],
            "Credit": ["", "14.54", "", "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.clean_dataframe(df)
        self.assertFalse(check[0])
        self.assertIn("Conflicting debit/credit information", check[1])

    def test_debit_only(self):
        """Tests the case where debit is the only money column"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Debit": ["-21.13", "-7.66", "-28.79", "1500.00"],
            "Description": ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        check = parse.clean_dataframe(df)
        self.assertTrue(check[0])
        self.assertIn("Amount", check[1].columns)
        self.assertNotIn("Debit", check[1].columns)

    def test_credit_only(self):
        """Tests the case where credit is the only money column"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Credit": ["21.13", "7.66", "-28.79", "1500.00"],
            "Description": ["GENOS STEAKS", "INSOMNIA COOKIES", "MCDONALD S", "Depost"]
        }
        df = pd.DataFrame(data)
        exp = [21.13, 7.66, -28.79, 1500.00]
        check = parse.clean_dataframe(df)
        self.assertTrue(check[0])
        self.assertIn("Amount", check[1].columns)
        self.assertNotIn("Credit", check[1].columns)
        for rx, ex in zip(check[1]["Amount"], exp):
            self.assertAlmostEqual(rx, ex)

    def test_column_conflict(self):
        """Tests the case when column labeling is conflicting"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": ["1773.85", "1766.19", "1737.40", "3237.40"]
        }
        df = pd.DataFrame(data)
        check = parse.clean_dataframe(df)
        self.assertFalse(check[0])
        self.assertIn("Could not determine column", check[1])

    def test_no_date_col(self):
        """Tests the case where no date column exists"""
        data = {
            "Amount": ["-21.13", "-7.66", "-28.79", "1500.00"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": ["1773.85", "1766.19", "1737.40", "3237.40"]
        }
        df = pd.DataFrame(data)
        with patch("builtins.input", return_value="Y"):
            check = parse.clean_dataframe(df)
        self.assertFalse(check[0])
        self.assertIn("Could not verify date columns", check[1])

    def test_no_money_col(self):
        """Tests the case where no amount, debit, or credit column exists"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": ["1773.85", "1766.19", "1737.40", "3237.40"]
        }
        df = pd.DataFrame(data)
        check = parse.clean_dataframe(df)
        self.assertFalse(check[0])
        self.assertIn("Could not determine column labeling", check[1])


if __name__ == "__main__":
    unittest.main()
