# Tiffany M. Mui
# Module 8 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for ancillary module
# Run with: pytest tests/test_ancillary.py -v


import sys
from pathlib import Path
from datetime import date
import pytest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


import Mui_Ancillary as aux


def mark_chart():
    """Returns simple matplotlib (figure, axes) for chart_save tests"""
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])
    chart = (fig, ax)
    return chart


@pytest.fixture(autouse=True)
def close_plot():
    """Closes charts after each test"""
    yield
    plt.close('all')


class TestDateCheck:
    """Class to test the dtg_check function"""


    def test_dtg_success(self):
        """Tests that a datetime object is returned when successful"""
        date_str = '2026-10-28'
        format_str = "%Y-%m-%d"
        check = aux.dtg_check(date_str, format_str)
        assert check[0]
        assert isinstance(check[1], date)


    def test_no_input(self):
        """Tests that no input returns an error and does not crash"""
        date_str = None
        format_str = "%Y-%m-%d"
        check = aux.dtg_check(date_str, format_str)
        assert not check[0]
        assert 'Invalid input' in check[1]


    def test_wrong_type(self):
        """Tests the case of wrong input type"""
        date_str = 'No Date'
        format_str = "%Y-%m-%d"
        check = aux.dtg_check(date_str, format_str)
        assert not check[0]
        assert 'Invalid input' in check[1]


    def test_not_date(self):
        """Tests the case when the date does not exist"""
        date_str = '2026-02-30'
        format_str = "%Y-%m-%d"
        check = aux.dtg_check(date_str, format_str)
        assert not check[0]
        assert 'Invalid input' in check[1]


class TestChartSave:
    """Class to test the chart_save function"""


    def test_save_success():
        """Tests that a chart was saved successfully"""
    def test_custom_dpi():
        """Tests that a custom dpi is accepted"""
    def test_bad_path():
        """Tests that nonexistent directory returns error"""
    def test_miss_ext():
        """Tests that a file name is a missing extension returns error"""