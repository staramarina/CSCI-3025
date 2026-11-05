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