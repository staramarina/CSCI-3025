# Tiffany M. Mui
# Module 7 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for the main program, Mui_M7Assignment.py
# Run with: pytest tests/test_wxr.py -v


import sys
from pathlib import Path
from unittest.mock import patch, MagicMock


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


import Mui_WxrHandle as wxr


# Sample data taken from a portion of a real response
SAMPLE_DATA = {
    'location': {
        'name': 'Colorado Springs',
        'region': 'Colorado',
        'country': 'United States of America'
    },
    'current': {
        'last_updated_epoch': 1793844000,
        'last_updated': '2026-11-04 19:00',
        'temp_f': 46.4,
        'condition': {
            'text': 'Thundery outbreaks in nearby',
            'code': 1087
        },
        'feels_like_f': 44.2
    },
    'forecast': {
        'forecastday': [{
            'date': '2026-11-04',
            'date_epoch': '1793750400',
            'day': {
                'maxtemp_f': 52.7,
                'mintemp_f': 32.7,
                'avgtemp_f': 43.4,
                'condition': {
                    'text': 'Sunny',
                    'code': 1000
                }
            }
        }]
    }
}


def make_response(data = None, json_err = None, http_err = None):
    """Returns a mock response object for requests
    
    Args:
        data: Mock data that would be received from the API
        json_err: JSON error to raise instead of returning
        http_err: HTTP error to raise instead of returning
    
    Returns:
        r: A MagicMock object that responds like a request
    """
    r = MagicMock()
    r.raise_for_status.return_value = None
    if None != json_err:
        r.json.side_effect = json_err
    elif None != http_err:
        r.raise_for_status.side_effect = http_err
    else:
        if None == data:
            r.json.return_value = sample_data()
        else:
            r.json.return_value = data
        return r


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


class TestWxrSuccess:
    """Class to test the successful path in wxr_api_call function"""


    @patch("wxr.requests.get")
    def test_return(self, mock_get):
        """Tests that a mock call returns mock JSON data"""
        mock_get.return_value = make_response()