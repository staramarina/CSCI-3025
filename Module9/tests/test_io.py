# Tiffany M. Mui
# Module 9 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for IO module
# Run with: python -m unittest tests.test_io -v


import unittest
import os
import sys
import tempfile
import logging
from pathlib import Path
from unittest.mock import patch
import pandas as pd
import matplotlib


matplotlib.use("Agg")
import matplotlib.pyplot as plt


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


import Mui_IO as io


def make_chart():
    """Returns simple matplotlib (figure, axes) for chart_save tests"""
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])
    chart = (fig, ax)
    return chart


class TestFileExists(unittest.TestCase):
    """Tests the file_exists function"""

    def setUp(self):
        """Setup method to create temporary testing directory"""
        self.__tmpdir = tempfile.TemporaryDirectory()
        self.tmp_dir = Path(self.__tmpdir.name)

    def tearDown(self):
        """Tear down method to delete temporary testing directory"""
        self.__tmpdir.cleanup()

    def test_file_exists_true(self):
        """Tests that (True, message) is returned when file exists"""
        test_file = self.tmp_dir / "exists.txt"
        test_file.write_text("Test Content\n")
        check = io.file_exists(str(test_file))
        self.assertTrue(check[0])
        self.assertIn("exists", check[1])

    def test_file_not_exists(self):
        """Tests that (False, message) is returned when file does not exist"""
        check = io.file_exists("not_file.txt")
        self.assertFalse(check[0])
        self.assertIn("does not exist", check[1])

    def test_directory(self):
        """Tests that path to directory returns (False, message)"""
        check = io.file_exists(str(self.tmp_dir))
        self.assertFalse(check[0])
        self.assertIn("not a file", check[1])


class TestCanWriteFile(unittest.TestCase):
    """Tests the can_write_file function"""

    def setUp(self):
        """Setup method to create temporary testing directory"""
        self.__tmpdir = tempfile.TemporaryDirectory()
        self.tmp_dir = Path(self.__tmpdir.name)

    def tearDown(self):
        """Tear down method to delete temporary testing directory"""
        self.__tmpdir.cleanup()

    def test_writable_dir(self):
        """Tests that writing to writable directory succeeds"""
        test_file = self.tmp_dir / "write_test.txt"
        check = io.can_write_file(str(test_file))
        self.assertTrue(check[0])
        self.assertIn("can be appended", check[1])

    def test_directory(self):
        """Tests that path to non-existent directory returns (False, message)"""
        temp_path = str(self.tmp_dir)
        dir_path = str(temp_path) + "/Missing Directory/write_test.txt"
        check = io.can_write_file(dir_path)
        self.assertFalse(check[0])
        self.assertIn("directory does not exist", check[1])


class TestDataframeCheck(unittest.TestCase):
    """Class to test dataframe_check(file_name, head_info=0) function"""

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
        with open(os.path.join(base, "malformed.csv"), "w") as f:
            f.write("Date,Description,MISSING\n")
            f.write("11/16/2026,INSOMNIA COOKIES,-7.66,1794.98\n")
            f.write("11/15/2026,Esso, Station,-20.27,1831.43\n")

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
        check = io.dataframe_check(file_name)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)

    def test_lead_rows(self):
        """Tests the case when there is a header and leading rows"""
        file_name = os.path.join(self.base, "good_lead.csv")
        head_info = 1
        check = io.dataframe_check(file_name, head_info)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)

    def test_no_head(self):
        """Tests the case when there is no header or leading rows"""
        file_name = os.path.join(self.base, "good_no_head.csv")
        head_info = None
        check = io.dataframe_check(file_name, head_info)
        self.assertTrue(check[0])
        self.assertIsInstance(check[1], pd.DataFrame)

    def test_no_file(self):
        """Tests the case when the file does not exist"""
        file_name = os.path.join(self.base, "not_here.csv")
        check = io.dataframe_check(file_name)
        self.assertFalse(check[0])
        self.assertIn("does not exist", check[1])

    def test_empty_file(self):
        """Tests the case when the file exists, but it's empty"""
        file_name = os.path.join(self.base, "empty.csv")
        check = io.dataframe_check(file_name)
        self.assertFalse(check[0])
        self.assertIn("no parsable data", check[1])

    def test_parse_err(self):
        """Tests that parsing error is returned if data is malformed"""
        file_name = os.path.join(self.base, "malformed.csv")
        check = io.dataframe_check(file_name)
        self.assertFalse(check[0])
        self.assertIn("Encountered parsing error", check[1])

    def test_val_err(self):
        """Tests that a value error is return if invalid header arg received"""
        file_name = os.path.join(self.base, "good_no_lead.csv")
        head_info = -1
        check = io.dataframe_check(file_name, head_info)
        self.assertFalse(check[0])
        self.assertIn("Encountered value error", check[1])


class TestChartSave(unittest.TestCase):
    """Class to test chart_save(chart, file_name, dpi=150) function"""

    def setUp(self):
        """Setup method to create temporary testing directory"""
        self.__tmpdir = tempfile.TemporaryDirectory()
        self.tmp_dir = Path(self.__tmpdir.name)
        self.chart = make_chart()

    def tearDown(self):
        """Tear down method to delete temporary testing directory"""
        plt.close("all")
        self.__tmpdir.cleanup()

    def test_save_success(self):
        """Tests that a chart was saved successfully"""
        chart = make_chart()
        file_name = self.tmp_dir / "test_chart.png"
        check = io.chart_save(chart, str(file_name))
        self.assertTrue(check[0])
        self.assertIn("saved", check[1])
        self.assertTrue(file_name.exists())

    def test_custom_dpi(self):
        """Tests that a custom dpi is accepted"""
        chart = make_chart()
        file_name = self.tmp_dir / "test_chart.png"
        check = io.chart_save(chart, str(file_name), dpi=300)
        self.assertTrue(check[0])
        self.assertIn("saved", check[1])
        self.assertTrue(file_name.exists())

    def test_bad_path(self):
        """Tests that nonexistent directory returns error"""
        chart = make_chart()
        file_name = self.tmp_dir / "Not Here" / "test_chart.png"
        check = io.chart_save(chart, str(file_name))
        self.assertFalse(check[0])
        self.assertIn("Failed to save", check[1])

    def test_miss_ext(self):
        """Tests that a file name with missing extension save as .png"""
        chart = make_chart()
        file_name = self.tmp_dir / "test_chart"
        save = self.tmp_dir / "test_chart.png"
        check = io.chart_save(chart, str(file_name))
        self.assertTrue(check[0])
        self.assertIn("saved", check[1])
        self.assertTrue(save.exists())


class TestFileInputHandle(unittest.TestCase):
    """Class to test the file_input_handle() function"""

    def setUp(self):
        """Setup method to create temporary testing directory"""
        self.__tmpdir = tempfile.TemporaryDirectory()
        self.tmp_dir = Path(self.__tmpdir.name)
        self.test_file = self.tmp_dir / "test.csv"
        self.test_file.write_text("Test Content\n")

    def tearDown(self):
        """Tear down method to delete temporary testing directory"""
        self.__tmpdir.cleanup()

    def test_file_there(self):
        """Tests that (True, message) is returned when file exists"""
        with patch("builtins.input", return_value=str(self.test_file)):
            check = io.file_input_handle()
        self.assertTrue(check[0])
        self.assertEqual(str(self.test_file), check[1])

    def test_file_not_there(self):
        """Tests that (False, message) is returned when file does not exist"""
        with patch("builtins.input", return_value="not_file.txt"):
            check = io.file_input_handle()
        self.assertFalse(check[0])
        self.assertIn("does not exist", check[1])


class TestLogSetup(unittest.TestCase):
    """Class to test the log_setup(log_file="log.txt") function"""

    def setUp(self):
        """Setup method to create temporary testing directory and logger"""
        self.__tmpdir = tempfile.TemporaryDirectory()
        self.log_file = os.path.join(self.__tmpdir.name, "test_log.txt")
        logging.getLogger("M9_Log").handlers.clear()

    def tearDown(self):
        """Tear down method to delete testing directory and clear logger"""
        logging.getLogger("M9_Log").handlers.clear()
        self.__tmpdir.cleanup()

    def test_handler(self):
        """Tests that the handler is attached to the shared logger"""
        log = io.log_setup(self.log_file)
        self.assertIs(logging.getLogger("M9_Log"), log)
        self.assertEqual(1, len(log.handlers))
        self.assertIsInstance(log.handlers[0], logging.FileHandler)
        self.assertEqual(self.log_file, log.handlers[0].baseFilename)
        self.assertEqual(logging.WARNING, log.level)

    def test_duplicate(self):
        """Tests that calling log_setup twice only results 
        in a single handler"""
        io.log_setup(self.log_file)
        io.log_setup(self.log_file)
        self.assertEqual(1, len(logging.getLogger("M9_Log").handlers))


class TestErrHandle(unittest.TestCase):
    """Class to test the err_handle(err_msg, err_log='log.txt') function"""

    def test_err_log_print(self):
        """Tests that error logs are printed correctly"""
        with self.assertLogs("M9_Log", level="ERROR") as capture:
            io.err_handle("Test fail message", "log.txt")
        self.assertEqual(len(capture.records), 1)
        record = capture.records[0]
        self.assertEqual(record.levelname, "ERROR")
        self.assertIn("Test fail message", record.getMessage())

    def test_err_log_console(self):
        """Tests the expected error message in the console"""
        with patch("builtins.print") as mock_print:
            io.err_handle("Test fail message", "log.txt")
        print_txt = " ".join(str(call.args[0]) 
                             for call in mock_print.call_args_list)
        self.assertIn("ERROR", print_txt)
        self.assertIn("log.txt", print_txt)


class TestWarnHandle(unittest.TestCase):
    """Class to test the warn_handle(warn_msg) function"""

    def test_warn_log_print(self):
        """Tests that warning logs are printed correctly"""
        with patch("builtins.input", return_value="N"), \
                self.assertLogs("M9_Log", level="WARNING") as capture:
            io.warn_handle("Test warn message")
        self.assertEqual(len(capture.records), 1)
        record = capture.records[0]
        self.assertEqual(record.levelname, "WARNING")
        self.assertIn("Test warn message", record.getMessage())

    def test_warn_log_console(self):
        """Tests the expected warning message in the console"""
        with patch("builtins.input", return_value="N") as mock_in, \
                self.assertLogs("M9_Log", level="WARNING"):
            io.warn_handle("Test warn message")
        prompt = mock_in.call_args.args[0]
        self.assertIn("Test warn message", prompt)
        self.assertIn("like to proceed (Y/N)", prompt)

    def test_force_confirm(self):
        """Tests the case when user confirms to continue processing"""
        warn_msg = "Test warning message"
        with patch("builtins.input", return_value="Y"), \
                self.assertLogs("M9_Log", level="WARNING"):
            check = io.warn_handle(warn_msg)
        self.assertTrue(check)

    def test_force_deny(self):
        """Tests the case when user declines to continue process"""
        warn_msg = "Test warning message"
        with patch("builtins.input", return_value="N"), \
                self.assertLogs("M9_Log", level="WARNING"):
            check = io.warn_handle(warn_msg)
        self.assertFalse(check)

    def test_force_low_confirm(self):
        """Tests that lower case y works to confirm continuing"""
        warn_msg = "Test warning message"
        with patch("builtins.input", return_value="y"), \
                self.assertLogs("M9_Log", level="WARNING"):
            check = io.warn_handle(warn_msg)
        self.assertTrue(check)


class TestPrinting(unittest.TestCase):
    """Class to test any printing-only functions"""

    def test_analysis_menu(self):
        """Tests the print_analysis_menu() function"""
        with patch("builtins.print") as mock_print:
            io.print_analysis_menu()
        txt = " ".join(str(call.args[0])
                       for call in mock_print.call_args_list)
        self.assertEqual(7, mock_print.call_count)
        exp = [
            'Please select one of the following options:',
            '1 -- Overall Spending per Day',
            '2 -- Spending by Category',
            '3 -- Spending by Description',
            '4 -- Overall Balance Changes per Day',
            '5 -- Top 5 Expenses',
            'x -- Quit'
        ]
        for item in exp:
            self.assertIn(item, txt)


if __name__ == "__main__":
    unittest.main()
