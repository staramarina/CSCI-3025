# Tiffany M. Mui
# Module 9 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for statement class module
# Run with: python -m unittest tests.test_statement -v


import unittest
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


import Mui_Statement as stmnt


class StmntBuild:
    """Class to build various statement class instances for test cases"""

    def build_lrg(self):
        """Builds and returns a larger pandas dataframe for analysis/charts"""
        data = {
            "Date": [
                "2026-10-27",
                "2026-10-21",
                "2026-10-13",
                "2026-10-13",
                "2026-10-06",
                "2026-10-05",
                "2026-10-05",
                "2026-09-28",
                "2026-09-21",
                "2026-09-11",
                "2026-09-08",
                "2026-09-03",
                "2026-09-03",
                "2026-09-03",
                "2026-09-03",
                "2026-08-27",
                "2026-08-20",
                "2026-08-18",
                "2026-08-11",
                "2026-08-06",
                "2026-08-03",
                "2026-08-03",
                "2026-08-01",
            ],
            "Amount": [
                -24.61,
                2651.68,
                -104.7,
                -39.51,
                2651.68,
                -3026.84,
                -197.91,
                -23.99,
                2651.68,
                -104.7,
                -41.51,
                -3026.84,
                -234.24,
                2964.26,
                2651.68,
                -22.71,
                2651.68,
                -39.59,
                -104.7,
                2651.68,
                -3026.84,
                -187.9,
                -59.31,
            ],
            "Category": [
                "Natural Gas",
                "Paycheck",
                "Internet",
                "Water",
                "Paycheck",
                "Uncategorized",
                "Electricity",
                "Natural Gas",
                "Paycheck",
                "Internet",
                "Water",
                "Transfer",
                "Electricity",
                "Uncategorized",
                "Paycheck",
                "Natural Gas",
                "Paycheck",
                "Water",
                "Internet",
                "Paycheck",
                "Uncategorized",
                "Electricity",
                "Uncategorized",
            ],
            "Description": [
                "Gas Company",
                "Workplace",
                "InternetCompany",
                "Locale Wa Utlpayment",
                "Workplace",
                "Newmortgage Company",
                "Locale",
                "Gas Company",
                "Workplace",
                "InternetCompany",
                "Locale Wa Utlpayment",
                "Newmortgage Company",
                "Locale",
                "Workplace Reimbursement",
                "Workplace",
                "Gas Company",
                "Workplace",
                "Locale Wa Utlpayment",
                "InternetCompany",
                "Workplace",
                "Newmortgage Company",
                "Locale",
                "Trash Company",
            ],
        }
        df = pd.DataFrame(data)
        df["Date"] = pd.to_datetime(df["Date"])
        df["Amount"] = pd.to_numeric(df["Amount"])
        return df

    def build_df6(self):
        """Builds and returns a pandas dataframe with 6 columns"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Post Date": ["", "11/17/2026", "11/16/2026", "11/16/2026"],
            "Amount": [-21.13, -7.66, -28.79, 1500.00],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": [54.12, 12.54, 5.37, 1505.37],
            "Category": ["Restaurants", "Restaurants", "Fast Food", "Income"],
        }
        df = pd.DataFrame(data)
        df["Date"] = pd.to_datetime(df["Date"])
        df["Post Date"] = pd.to_datetime(df["Post Date"])
        df["Amount"] = pd.to_numeric(df["Amount"])
        df["Balance"] = pd.to_numeric(df["Balance"])
        return df

    def build_df4(self):
        """Builds and returns a pandas dataframe with 4 columns"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Amount": [-21.13, -7.66, -28.79, 1500.00],
            "Description": ["GENOS STEAKS", "COOKIES", "MCDONALD S", "Depost"],
            "Balance": [1773.85, 1766.19, 1737.40, 3237.40],
        }
        df = pd.DataFrame(data)
        df["Date"] = pd.to_datetime(df["Date"])
        df["Amount"] = pd.to_numeric(df["Amount"])
        df["Balance"] = pd.to_numeric(df["Balance"])
        return df

    def build_min(self):
        """Builds and returns a pandas dataframe with only Date and Amount"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Amount": [-21.13, -7.66, -28.79, 1500.00],
        }
        df = pd.DataFrame(data)
        df["Date"] = pd.to_datetime(df["Date"])
        df["Amount"] = pd.to_numeric(df["Amount"])
        return df

    def build_nan(self):
        """Builds and returns a dataframe with all columns, but np.nan data"""
        data = {
            "Date": ["11/18/2026", "11/16/2026", "11/16/2026", "11/15/2026"],
            "Amount": [np.nan, np.nan, np.nan, np.nan],
            "Description": [np.nan, np.nan, np.nan, np.nan],
            "Balance": [np.nan, np.nan, np.nan, np.nan],
            "Category": [np.nan, np.nan, np.nan, np.nan],
        }
        df = pd.DataFrame(data)
        df["Date"] = pd.to_datetime(df["Date"])
        return df

    def build_default_stmnt(self):
        """Builds a default statement instance"""
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

    def build_any_stmnt(self, df, name):
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

    def test_string_method(self):
        """Tests that the __str__ method returns name and data"""
        txt = str(self.stmnt6)
        self.assertIn("Transactions Test 1.csv", txt)
        self.assertIn("COOKIES", txt)
        self.assertIn("Amount", txt)

    def test_add_method(self):
        """Tests that the __add__ method returns a new combined instance"""
        new_stmnt = self.stmnt4 + self.stmnt6
        self.assertIn("Post Date", new_stmnt.df.columns)
        self.assertEqual(8, len(new_stmnt.df))


class TestSpendAnalysis(StmntBuild, unittest.TestCase):
    """Class to test the spend_analysis() method"""

    def setUp(self):
        """Setup method to create test statement class instances"""
        name_nan = "np.nan test"
        df = self.build_nan()
        self.stmnt_nan = self.build_any_stmnt(df, name_nan)
        self.stmnt4 = self.build_df4_stmnt()

    def test_spend_income(self):
        """Tests that income is excluded from expenses"""
        check = self.stmnt4.spend_analysis()
        df = check[1][0]
        self.assertTrue(check[0])
        self.assertTrue((df["Amount"] >= 0).all())

    def test_spend_pad(self):
        """Tests that missing dates are added"""
        check = self.stmnt4.spend_analysis()
        df = check[1][0]
        day = df[df["Date"] == pd.Timestamp("2026-11-17")]
        self.assertEqual(3, len(df))
        self.assertEqual(1, len(day))
        self.assertAlmostEqual(0.0, day["Amount"].iloc[0])

    def test_spend_stats(self):
        """Tests than min, max, and avg values are calculated correctly"""
        check = self.stmnt4.spend_analysis()
        data = check[1]
        exp_min = 0.0
        exp_max = 7.66 + 28.79
        exp_avg = (21.13 + 7.66 + 28.79) / 3
        self.assertAlmostEqual(exp_min, data[1], places=2)
        self.assertAlmostEqual(exp_max, data[2], places=2)
        self.assertAlmostEqual(exp_avg, data[3], places=2)

    def test_spend_nan(self):
        """Tests the case when all data is nan"""
        check = self.stmnt_nan.spend_analysis()
        self.assertFalse(check[0])
        self.assertIn("No data available for analysis", check[1])

    def test_spend_orig(self):
        """Tests that the original dataframe is unmodified"""
        orig = self.stmnt4.df.copy(deep=True)
        self.stmnt4.spend_analysis()
        pd.testing.assert_frame_equal(orig, self.stmnt4.df)


class TestSpendChart(StmntBuild, unittest.TestCase):
    """Class to test the spend_chart() method"""

    def setUp(self):
        """Setup method to create test statement class instances"""
        name_nan = "np.nan test"
        df = self.build_nan()
        self.stmnt_nan = self.build_any_stmnt(df, name_nan)
        self.stmnt4 = self.build_df4_stmnt()

    def tearDown(self):
        """Closes charts after each test"""
        plt.close("all")

    def test_spend_fig(self):
        """Tests that both figure and axes is returned"""
        check = self.stmnt4.spend_chart()
        fig, ax = check[1]
        self.assertTrue(check[0])
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_spend_label(self):
        """Tests that the chart title and axis label are correct"""
        check = self.stmnt4.spend_chart()
        ax = check[1][1]
        self.assertIn("Aggregate Expenses per Day", ax.get_title())
        self.assertIn("Date", ax.get_xlabel())
        self.assertIn("Aggregate Amount", ax.get_ylabel())

    def test_spend_legend(self):
        """Tests that all legend items are present"""
        check = self.stmnt4.spend_chart()
        ax = check[1][1]
        legend_txt = []
        for text in ax.get_legend().get_texts():
            legend_txt.append(text.get_text())
        self.assertEqual(4, len(legend_txt))
        self.assertIn("Daily Expense Total", legend_txt[0])
        self.assertIn("Maximum Daily Expense", legend_txt[1])
        self.assertIn("Average Daily Expense", legend_txt[2])
        self.assertIn("Minimum Daily Expense", legend_txt[3])

    def test_spend_chart_nan(self):
        """Tests the case when all data is nan"""
        check = self.stmnt_nan.spend_chart()
        self.assertFalse(check[0])
        self.assertIn("No data available for analysis", check[1])


class TestCatAnalysis(StmntBuild, unittest.TestCase):
    """Class to test the cat_analysis() method"""

    def setUp(self):
        """Setup method to create test statement class instances"""
        name2 = "Error Testing"
        df2 = self.build_min()
        self.stmnt2 = self.build_any_stmnt(df2, name2)
        name_nan = "np.nan test"
        df = self.build_nan()
        self.stmnt_nan = self.build_any_stmnt(df, name_nan)
        self.stmnt6 = self.build_df6_stmnt()

    def test_cat_income(self):
        """Tests that income is excluded from expenses"""
        check = self.stmnt6.cat_analysis()
        df = check[1]
        self.assertTrue(check[0])
        self.assertTrue((df["Amount"] >= 0).all())

    def test_cat_agg(self):
        """Tests that amount values are aggregated"""
        check = self.stmnt6.cat_analysis()
        df = check[1]
        self.assertTrue(check[0])
        self.assertEqual(2, len(df))

    def test_cat_sort(self):
        """Tests that categories are sorted by amount"""
        check = self.stmnt6.cat_analysis()
        df = check[1]
        exp_res = 21.13 + 7.66
        exp_ff = 28.79
        self.assertTrue(check[0])
        self.assertAlmostEqual(exp_ff, df.loc[0, "Amount"])
        self.assertAlmostEqual(exp_res, df.loc[1, "Amount"])
        self.assertLessEqual(df.loc[0, "Amount"], df.loc[1, "Amount"])

    def test_cat_err(self):
        """Tests the case when there is no Category column"""
        check = self.stmnt2.cat_analysis()
        self.assertFalse(check[0])
        self.assertIn("Category data not available", check[1])

    def test_cat_nan(self):
        """Tests the case when all data is nan"""
        check = self.stmnt_nan.cat_analysis()
        self.assertFalse(check[0])
        self.assertIn("No data available for analysis", check[1])

    def test_cat_orig(self):
        """Tests that the original dataframe is unmodified"""
        orig = self.stmnt6.df.copy(deep=True)
        self.stmnt6.cat_analysis()
        pd.testing.assert_frame_equal(orig, self.stmnt6.df)


class TestCatChart(StmntBuild, unittest.TestCase):
    """Class to test the cat_chart() method"""

    def setUp(self):
        """Setup method to create test statement class instances"""
        name2 = "Error Testing"
        df2 = self.build_min()
        self.stmnt2 = self.build_any_stmnt(df2, name2)
        name_nan = "np.nan test"
        df = self.build_nan()
        self.stmnt_nan = self.build_any_stmnt(df, name_nan)
        self.stmnt6 = self.build_df6_stmnt()

    def tearDown(self):
        """Closes charts after each test"""
        plt.close("all")

    def test_cat_fig(self):
        """Tests that both figure and axes is returned"""
        check = self.stmnt6.cat_chart()
        fig, ax = check[1]
        self.assertTrue(check[0])
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_cat_label(self):
        """Tests that the chart title and axis label are correct"""
        check = self.stmnt6.cat_chart()
        fig, ax = check[1]
        self.assertTrue(check[0])
        self.assertIn("Total Expenses by Category", ax.get_title())
        self.assertIn("Total Amount", ax.get_xlabel())

    def test_cat_chart_err(self):
        """Tests the case when Category is not a column"""
        check = self.stmnt2.cat_chart()
        self.assertFalse(check[0])
        self.assertIn("Category data not available", check[1])

    def test_cat_chart_nan(self):
        """Tests the case when all data is nan"""
        check = self.stmnt_nan.cat_chart()
        self.assertFalse(check[0])
        self.assertIn("No data available for analysis", check[1])


class TestDescriptAnalysis(StmntBuild, unittest.TestCase):
    """Class to test the descript_analysis() method"""

    def setUp(self):
        """Setup method to create test statement class instances"""
        name2 = "Error Testing"
        df2 = self.build_min()
        self.stmnt2 = self.build_any_stmnt(df2, name2)
        name_nan = "np.nan test"
        df = self.build_nan()
        self.stmnt_nan = self.build_any_stmnt(df, name_nan)
        self.stmnt6 = self.build_df6_stmnt()

    def test_descript_income(self):
        """Tests that income is excluded from expenses"""
        check = self.stmnt6.descript_analysis()
        df = check[1]
        self.assertTrue(check[0])
        self.assertTrue((df["Amount"] >= 0).all())

    def test_descript_sort(self):
        """Tests that descriptions are sorted by amount"""
        check = self.stmnt6.descript_analysis()
        df = check[1]
        exp_stk = 21.13
        exp_cook = 7.66
        exp_mac = 28.79
        self.assertTrue(check[0])
        self.assertEqual(3, len(df))
        self.assertAlmostEqual(exp_cook, df.loc[0, "Amount"])
        self.assertAlmostEqual(exp_stk, df.loc[1, "Amount"])
        self.assertAlmostEqual(exp_mac, df.loc[2, "Amount"])
        self.assertLessEqual(df.loc[0, "Amount"], df.loc[1, "Amount"])
        self.assertLessEqual(df.loc[1, "Amount"], df.loc[2, "Amount"])

    def test_descript_err(self):
        """Tests the case when there is no Description column"""
        check = self.stmnt2.descript_analysis()
        self.assertFalse(check[0])
        self.assertIn("Description data not available", check[1])

    def test_descript_nan(self):
        """Tests the case when all data is nan"""
        check = self.stmnt_nan.descript_analysis()
        self.assertFalse(check[0])
        self.assertIn("No data available for analysis", check[1])

    def test_descript_orig(self):
        """Tests that the original dataframe is unmodified"""
        orig = self.stmnt6.df.copy(deep=True)
        self.stmnt6.descript_analysis()
        pd.testing.assert_frame_equal(orig, self.stmnt6.df)


class TestDescriptChart(StmntBuild, unittest.TestCase):
    """Class to test the descript_chart() method"""

    def setUp(self):
        """Setup method to create test statement class instances"""
        name2 = "Error Testing"
        df2 = self.build_min()
        self.stmnt2 = self.build_any_stmnt(df2, name2)
        name_nan = "np.nan test"
        df = self.build_nan()
        self.stmnt_nan = self.build_any_stmnt(df, name_nan)
        self.stmnt6 = self.build_df6_stmnt()

    def tearDown(self):
        """Closes charts after each test"""
        plt.close("all")

    def test_descript_fig(self):
        """Tests that both figure and axes is returned"""
        check = self.stmnt6.descript_chart()
        fig, ax = check[1]
        self.assertTrue(check[0])
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_descript_label(self):
        """Tests that the chart title and axis label are correct"""
        check = self.stmnt6.descript_chart()
        fig, ax = check[1]
        self.assertTrue(check[0])
        self.assertIn("Total Expenses by Description", ax.get_title())
        self.assertIn("Total Amount", ax.get_xlabel())

    def test_descript_chart_err(self):
        """Tests the case when Description is not a column"""
        check = self.stmnt2.descript_chart()
        self.assertFalse(check[0])
        self.assertIn("Description data not available", check[1])

    def test_descript_chart_nan(self):
        """Tests the case when all data is nan"""
        check = self.stmnt_nan.descript_chart()
        self.assertFalse(check[0])
        self.assertIn("No data available for analysis", check[1])


class TestBalAnalysis(StmntBuild, unittest.TestCase):
    """Class to test the bal_analysis() method"""

    def setUp(self):
        """Setup method to create test statement class instances"""
        name2 = "Error Testing"
        df2 = self.build_min()
        self.stmnt2 = self.build_any_stmnt(df2, name2)
        name_nan = "np.nan test"
        df = self.build_nan()
        self.stmnt_nan = self.build_any_stmnt(df, name_nan)
        self.stmnt4 = self.build_df4_stmnt()

    def test_bal_max(self):
        """Tests that balance values only reflect maximum"""
        check = self.stmnt4.bal_analysis()
        df = check[1][0]
        exp_bal = [3237.40, 1766.19, 1773.85]
        self.assertTrue(check[0])
        self.assertEqual(3, len(df))
        for rx, ex in zip(df["Balance"], exp_bal):
            self.assertAlmostEqual(rx, ex)

    def test_bal_stats(self):
        """Tests than avg value is calculated correctly"""
        check = self.stmnt4.bal_analysis()
        df, avg = check[1]
        exp_avg = (3237.40 + 1766.19 + 1773.85) / 3
        self.assertTrue(check[0])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertAlmostEqual(exp_avg, avg, places=2)

    def test_bal_err(self):
        """Tests the case when there is no Balance column"""
        check = self.stmnt2.bal_analysis()
        self.assertFalse(check[0])
        self.assertIn("Balance data not available", check[1])

    def test_bal_nan(self):
        """Tests the case when all data is nan"""
        check = self.stmnt_nan.bal_analysis()
        self.assertFalse(check[0])
        self.assertIn("No data available for analysis", check[1])

    def test_bal_orig(self):
        """Tests that the original dataframe is unmodified"""
        orig = self.stmnt4.df.copy(deep=True)
        self.stmnt4.bal_analysis()
        pd.testing.assert_frame_equal(orig, self.stmnt4.df)


class TestBalChart(StmntBuild, unittest.TestCase):
    """Class to test the bal_chart() method"""

    def setUp(self):
        """Setup method to create test statement class instances"""
        name2 = "Error Testing"
        df2 = self.build_min()
        self.stmnt2 = self.build_any_stmnt(df2, name2)
        name_nan = "np.nan test"
        df = self.build_nan()
        self.stmnt_nan = self.build_any_stmnt(df, name_nan)
        self.stmnt4 = self.build_df4_stmnt()

    def tearDown(self):
        """Closes charts after each test"""
        plt.close("all")

    def test_bal_fig(self):
        """Tests that both figure and axes is returned"""
        check = self.stmnt4.bal_chart()
        fig, ax = check[1]
        self.assertTrue(check[0])
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_bal_label(self):
        """Tests that the chart title and axis label are correct"""
        check = self.stmnt4.bal_chart()
        fig, ax = check[1]
        self.assertIn("Maximum Balance per Day", ax.get_title())
        self.assertIn("Date", ax.get_xlabel())
        self.assertIn("Balance", ax.get_ylabel())

    def test_bal_legend(self):
        """Tests that all legend items are present"""
        check = self.stmnt4.bal_chart()
        fig, ax = check[1]
        legend_txt = []
        for text in ax.get_legend().get_texts():
            legend_txt.append(text.get_text())
        self.assertEqual(2, len(legend_txt))
        self.assertIn("Maximum Daily Balance", legend_txt[0])
        self.assertIn("Average Maximum Balance", legend_txt[1])

    def test_bal_chart_err(self):
        """Tests the case when Balance is not a column"""
        check = self.stmnt2.bal_chart()
        self.assertFalse(check[0])
        self.assertIn("Balance data not available", check[1])

    def test_bal_chart_nan(self):
        """Tests the case when all data is nan"""
        check = self.stmnt_nan.bal_chart()
        self.assertFalse(check[0])
        self.assertIn("No data available for analysis", check[1])


class TestTopAnalysis(StmntBuild, unittest.TestCase):
    """Class to test the top5_analysis() method"""

    def setUp(self):
        """Setup method to create test statement class instances"""
        name2 = "Error Testing"
        df2 = self.build_min()
        name_big = "Large Testing"
        df_big = self.build_lrg()
        self.stmnt2 = self.build_any_stmnt(df2, name2)
        self.stmnt_lrg = self.build_any_stmnt(df_big, name_big)
        name_nan = "np.nan test"
        df = self.build_nan()
        self.stmnt_nan = self.build_any_stmnt(df, name_nan)
        self.stmnt6 = self.build_df6_stmnt()

    def test_top_income(self):
        """Tests that income is excluded from expenses"""
        check = self.stmnt6.top5_analysis()
        df = check[1]
        self.assertTrue(check[0])
        self.assertTrue((df["Amount"] >= 0).all())

    def test_top_sort(self):
        """Tests that descriptions are sorted by amount"""
        check = self.stmnt6.top5_analysis()
        df = check[1]
        exp_stk = 21.13
        exp_cook = 7.66
        exp_mac = 28.79
        self.assertTrue(check[0])
        self.assertEqual(3, len(df))
        self.assertAlmostEqual(exp_mac, df.loc[0, "Amount"])
        self.assertAlmostEqual(exp_stk, df.loc[1, "Amount"])
        self.assertAlmostEqual(exp_cook, df.loc[2, "Amount"])
        self.assertLessEqual(df.loc[2, "Amount"], df.loc[1, "Amount"])
        self.assertLessEqual(df.loc[1, "Amount"], df.loc[0, "Amount"])

    def test_top_less(self):
        """Tests the case when there are less than five descriptions"""
        check = self.stmnt6.top5_analysis()
        df = check[1]
        exp_tot = 21.13 + 7.66 + 28.79
        self.assertTrue(check[0])
        self.assertEqual(3, len(df))
        self.assertNotIn("Other", df["Description"].values)
        self.assertAlmostEqual(exp_tot, df["Amount"].sum())

    def test_top_more(self):
        """Tests the case when there are more than five descriptions"""
        check = self.stmnt_lrg.top5_analysis()
        df = check[1]
        exp_gas = 24.61 + 23.99 + 22.71
        exp_www = 104.7 + 104.7 + 104.7
        exp_water = 39.51 + 41.51 + 39.59
        exp_mort = 3026.84 + 3026.84 + 3026.84
        exp_elec = 197.91 + 234.24 + 187.9
        exp_other = 59.31
        self.assertTrue(check[0])
        self.assertEqual(6, len(df))
        self.assertIn("Other", df["Description"].values)
        indx = df.set_index("Description")
        self.assertAlmostEqual(
            exp_gas, indx.loc["Gas Company", "Amount"], places=2
        )
        self.assertAlmostEqual(
            exp_www, indx.loc["InternetCompany", "Amount"], places=2
        )
        self.assertAlmostEqual(
            exp_water, indx.loc["Locale Wa Utlpayment", "Amount"], places=2
        )
        self.assertAlmostEqual(
            exp_mort, indx.loc["Newmortgage Company", "Amount"], places=2
        )
        self.assertAlmostEqual(
            exp_elec, indx.loc["Locale", "Amount"], places=2
        )
        self.assertAlmostEqual(
            exp_other, indx.loc["Other", "Amount"], places=2
        )

    def test_top_err(self):
        """Tests the case when there is no Description column"""
        check = self.stmnt2.top5_analysis()
        self.assertFalse(check[0])
        self.assertIn("Description data not available", check[1])

    def test_top_nan(self):
        """Tests the case when all data is nan"""
        check = self.stmnt_nan.top5_analysis()
        self.assertFalse(check[0])
        self.assertIn("No data available for analysis", check[1])

    def test_top_orig(self):
        """Tests that the original dataframe is unmodified"""
        orig = self.stmnt6.df.copy(deep=True)
        self.stmnt6.top5_analysis()
        pd.testing.assert_frame_equal(orig, self.stmnt6.df)


class TestTopChart(StmntBuild, unittest.TestCase):
    """Class to test the top5_chart() method"""

    def setUp(self):
        """Setup method to create test statement class instances"""
        name2 = "Error Testing"
        df2 = self.build_min()
        name_big = "Large Testing"
        df_big = self.build_lrg()
        self.stmnt2 = self.build_any_stmnt(df2, name2)
        self.stmnt_lrg = self.build_any_stmnt(df_big, name_big)
        name_nan = "np.nan test"
        df = self.build_nan()
        self.stmnt_nan = self.build_any_stmnt(df, name_nan)
        self.stmnt6 = self.build_df6_stmnt()

    def tearDown(self):
        """Closes charts after each test"""
        plt.close("all")

    def test_top_fig(self):
        """Tests that both figure and axes is returned"""
        check = self.stmnt6.top5_chart()
        fig, ax = check[1]
        self.assertTrue(check[0])
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_top_label(self):
        """Tests that the chart title is correct"""
        check = self.stmnt6.top5_chart()
        fig, ax = check[1]
        self.assertTrue(check[0])
        self.assertIn("Top 5 Expenses", ax.get_title())

    def test_top_less_chart(self):
        """Tests that less than 5 wedges are included"""
        check = self.stmnt6.top5_chart()
        fig, ax = check[1]
        self.assertEqual(3, len(ax.patches))

    def test_top_more_chart(self):
        """Tests that 6 wedges are included"""
        check = self.stmnt_lrg.top5_chart()
        fig, ax = check[1]
        self.assertEqual(6, len(ax.patches))

    def test_top_chart_err(self):
        """Tests the case when Description is not a column"""
        check = self.stmnt2.top5_chart()
        self.assertFalse(check[0])
        self.assertIn("Description data not available", check[1])

    def test_top_chart_nan(self):
        """Tests the case when all data is nan"""
        check = self.stmnt_nan.top5_chart()
        self.assertFalse(check[0])
        self.assertIn("No data available for analysis", check[1])


if __name__ == "__main__":
    unittest.main()
