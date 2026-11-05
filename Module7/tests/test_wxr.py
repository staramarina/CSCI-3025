# Tiffany M. Mui
# Module 7 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for the main program, Mui_M7Assignment.py
# Run with: pytest tests/test_wxr.py -v


import sys
from pathlib import Path


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


import Mui_WxrHandle as wxr


class TestEnvURL:
    """Class to test pulling the API key and building the query URLs"""


    def test_pull_key(self):
        """Tests pulling the API key from the env file"""
        key = wxr.load_env()
        assert None != key


    def test_url_good(self):
        """Tests building the URL to pull forecast weather data
        
        Args:
        
        Returns:
        """
        key = '0123456789'
        loc = 'Manassas'
        days = '3'
        url = wxr.build_url(key, loc, days)
        assert 'weatherapi' in url
        assert 'forecast' in url
        assert key in url
        assert loc in url
        assert days in url


    def test_url_defaults(self):
        """Tests that default values are applied if not supplied"""
        key = '0123456789'
        url = wxr.build_url(key)
        assert 'weatherapi' in url
        assert 'forecast' in url
        assert key in url
        assert 'London' in url
        assert '7' in url


class TestLocation:
    """Class to test formatting the location variable"""

    def test_single_word(self):
        """Tests the loc_parsing with the case of a single word"""
        raw = 'Manassas'
        loc = wxr.loc_parsing(raw)
        assert raw in loc


    def test_multiple_word(self):
        """Tests the loc_parsing with the case of multiple words"""
        raw = 'Colorado Springs'
        loc = wxr.loc_parsing(raw)
        assert 'Colorado' in loc
        assert '+' in loc
        assert 'Springs' in loc


    def test_mixed_case(self):
        """Tests the loc_parsing with the case multiple words of mixed case"""
        raw = 'New YORK cItY'
        loc = wxr.loc_parsing(raw)
        assert 'New' in loc
        assert 'York' in loc
        assert 'City' in loc
        assert '+' in loc


    def test_empty(self):
        """Tests the loc_parsing with the case of an empty string"""
        raw = ''
        loc = wxr.loc_parsing(raw)
        assert '' == loc


    def test_number(self):
        """Tests the loc_parsing with the case of a number"""
        raw = 96786
        loc = wxr.loc_parsing(raw)
        assert '96786' in loc