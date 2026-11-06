# Tiffany M. Mui
# Module 7 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for the main program, Mui_M7Assignment.py
# Run with: pytest tests/test_wxr.py -v


import sys
from pathlib import Path
from copy import deepcopy
import pytest
from unittest.mock import patch, MagicMock
import requests


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
        'feelslike_f': 44.2
    },
    'forecast': {
        'forecastday': [
            {
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
            }, {
            'date': '2026-11-05',
            'date_epoch': '1793836800',
            'day': {
                'maxtemp_f': 54.1,
                'mintemp_f': 31.8,
                'avgtemp_f': 43.6,
                'condition': {
                    'text': 'Sunny',
                    'code': 1000
                }
            }
            }
        ]
    }
}
META_KEYS = ('name', 'region', 'country', 'last', 'temp_now', 
             'feels', 'con_text')
SAMPLE_URL = "https://api.weatherapi.com/v1/x.json"


@pytest.fixture
def sample_json():
    """Returns a deepcopy of SAMPLE_DATA to prevent modification"""
    return deepcopy(SAMPLE_DATA)


@pytest.fixture
def parsed(sample_json):
    """Returns a parsed data set using json_parsing function"""
    data = wxr.json_parsing(sample_json)
    return data


@pytest.fixture
def print_out(capsys, parsed):
    """Returns read out data of a fresh sample_json"""
    wxr.wxr_display(deepcopy(parsed))
    return capsys.readouterr().out


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
            r.json.return_value = SAMPLE_DATA
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


    @patch("Mui_WxrHandle.requests.get")
    def test_return(self, mock_get):
        """Tests that a mock call returns mock JSON data"""
        mock_get.return_value = make_response()
        data = wxr.wxr_api_call(SAMPLE_URL)
        assert SAMPLE_DATA == data


    @patch("Mui_WxrHandle.requests.get")
    def test_timeout_default(self, mock_get):
        """Tests that the timeout is the default if not specified"""
        mock_get.return_value = make_response()
        wxr.wxr_api_call(SAMPLE_URL)
        mock_get.assert_called_once_with(SAMPLE_URL, timeout=10)


    @patch("Mui_WxrHandle.requests.get")
    def test_timeout_specified(self, mock_get):
        """Tests that the specified timeout is used when given"""
        mock_get.return_value = make_response()
        wxr.wxr_api_call(SAMPLE_URL, timeout=5)
        mock_get.assert_called_once_with(SAMPLE_URL, timeout=5)


class TestWxrTimeout:
    """Class to test the timeout path in wxr_api_call function"""


    @patch("Mui_WxrHandle.requests.get")
    def test_timeout_return(self, mock_get, tmp_path):
        """Tests that a timeout causes exit with code 1"""
        mock_get.side_effect = requests.exceptions.Timeout
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit) as exc_info:
            wxr.wxr_api_call(SAMPLE_URL, err_log=str(log_file))
        assert 1 == exc_info.value.code


    @patch("Mui_Logging.print_log")
    @patch("Mui_WxrHandle.requests.get")
    def test_timeout_print(self, mock_get, mock_print_log, capsys, tmp_path):
        """Tests that a timeout is logged and printed error points to logs"""
        mock_get.side_effect = requests.exceptions.Timeout(
                "Connection timed out")
        mock_print_log.return_value = (True, "File printed successfully")
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit):
            wxr.wxr_api_call(SAMPLE_URL, err_log=str(log_file))
        mock_print_log.assert_called_once()
        args, _ = mock_print_log.call_args
        assert isinstance(args[0], requests.exceptions.Timeout)
        assert str(log_file) == args[1]
        captured = capsys.readouterr()
        assert "An error occurred with the Weather API" in captured.out
        assert "See" in captured.out
        assert str(log_file) in captured.out


class TestWxrHTTP:
    """Class to test the HTTP error path in wxr_api_call function"""


    @patch("Mui_WxrHandle.requests.get")
    def test_http_none(self, mock_get, tmp_path):
        """Tests that an HTTP error causes exit with code 1"""
        err = requests.exceptions.HTTPError("401 Client Error: Unauthorized "
                "for url: https://api.weatherapi.com/v1/")
        mock_get.return_value = make_response(http_err=err)
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit) as exc_info:
            wxr.wxr_api_call(SAMPLE_URL, err_log=str(log_file))
        assert 1 == exc_info.value.code


    @patch("Mui_Logging.print_log")
    @patch("Mui_WxrHandle.requests.get")
    def test_http_error(self, mock_get, mock_print_log, capsys, tmp_path):
        """Tests that HTTP error is logged and printed error points to logs"""
        err = requests.exceptions.HTTPError("401 Client Error")
        mock_get.return_value = make_response(http_err=err)
        mock_print_log.return_value = (True, "File printed successfully")
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit):
            wxr.wxr_api_call(SAMPLE_URL, err_log=str(log_file))
        mock_print_log.assert_called_once()
        args, _ = mock_print_log.call_args
        assert isinstance(args[0], requests.exceptions.HTTPError)
        assert str(log_file) == args[1]
        captured = capsys.readouterr()
        assert "An error occurred with the Weather API" in captured.out
        assert "See" in captured.out
        assert str(log_file) in captured.out


class TestWxrRequest:
    """Class to test the request exception path in wxr_api_call function"""


    @patch("Mui_WxrHandle.err_handle")
    @patch("Mui_WxrHandle.requests.get")
    def test_connect_none(self, mock_get, mock_log, tmp_path):
        """Tests that a connection failure causes exit with code 1"""
        mock_get.side_effect = requests.exceptions.ConnectionError(
                "Connection refused")
        mock_log.return_value = (True, "File printed successfully")
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit) as exc_info:
            wxr.wxr_api_call(SAMPLE_URL, err_log=str(log_file))
        assert 1 == exc_info.value.code


    @patch("Mui_Logging.print_log")
    @patch("Mui_WxrHandle.requests.get")
    def test_req_err(self, mock_get, mock_print_log, capsys, tmp_path):
        """Tests that request error is logged and reported"""
        mock_get.side_effect = requests.exceptions.ConnectionError(
                "Connection refused")
        mock_print_log.return_value = (True, "File printed successfully")
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit):
            wxr.wxr_api_call(SAMPLE_URL, err_log=str(log_file))
        mock_print_log.assert_called_once()
        captured = capsys.readouterr()
        assert "An error occurred with the Weather API" in captured.out
        assert "See" in captured.out
        assert str(log_file) in captured.out


class TestWxrJSON:
    """Class to test the value error path in wxr_api_call function"""


    @patch("Mui_WxrHandle.requests.get")
    def test_json_none(self, mock_get, tmp_path):
        """Tests that bad JSON data causes exit with code 1"""
        err = ValueError("Expecting value: line 1 column 1")
        mock_get.return_value = make_response(json_err=err)
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit) as exc_info:
            wxr.wxr_api_call(SAMPLE_URL, err_log=str(log_file))
        assert 1 == exc_info.value.code


    @patch("Mui_Logging.print_log")
    @patch("Mui_WxrHandle.requests.get")
    def test_json_err(self, mock_get, mock_print_log, capsys, tmp_path):
        """Tests that bad JSON data error is logged and reported"""
        err = ValueError("Expecting value: line 1 column 1")
        mock_get.return_value = make_response(json_err=err)
        mock_print_log.return_value = (True, "File printed successfully")
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit):
            wxr.wxr_api_call(SAMPLE_URL, err_log=str(log_file))
        mock_print_log.assert_called_once()
        captured = capsys.readouterr()
        assert "An error occurred with the Weather API" in captured.out
        assert "See" in captured.out
        assert str(log_file) in captured.out


class TestJSONParsing:
    """Class to test the json_parsing function"""


    def test_single_values(self, parsed):
        """Tests that single values are placed into the dictionary"""
        for key in META_KEYS:
            assert key in parsed
        assert 'Colorado Springs' == parsed['name']
        assert 'Colorado' == parsed['region']
        assert 'United States of America' == parsed['country']
        assert '2026-11-04 19:00' == parsed['last']
        assert 46.4 == parsed['temp_now']
        assert 44.2 == parsed['feels']
        assert 'Thundery outbreaks in nearby' == parsed['con_text']


    def test_variable_keys(self, parsed):
        """Tests that variable date keys are placed into the dictionary"""
        assert '2026-11-04' in parsed
        assert '2026-11-05' in parsed


    @pytest.mark.parametrize(
        "date, expected", [
            ('2026-11-04', [52.7, 32.7, 'Sunny']),
            ('2026-11-05', [54.1, 31.8, 'Sunny'])
        ]
    )


    def test_day_values(self, parsed, date, expected):
        """Tests that values for date keys are present as expected"""
        assert expected == parsed[date]


    @patch("Mui_Logging.print_log")
    def test_key_missing(self, mock_print_log, capsys, tmp_path, sample_json):
        """Tests that KeyError is caught when parsing JSON"""
        del sample_json['current']
        mock_print_log.return_value = (True, "File printed successfully")
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit) as exc_info:
            wxr.json_parsing(sample_json, err_log=str(log_file))
        assert 1 == exc_info.value.code
        mock_print_log.assert_called_once()
        captured = capsys.readouterr()
        assert "An error occurred with the Weather API" in captured.out
        assert "See" in captured.out
        assert str(log_file) in captured.out


class TestWxrDisplay:
    """Class to test the wxr_display function"""


    def test_current_contents(self, print_out):
        """Tests that locations and current weather data print"""
        assert ('Location: Colorado Springs, Colorado, '
                'United States of America') in print_out
        assert 'Current Condition: Thundery outbreaks in nearby' in print_out
        assert f'Current Temperature: 46.4\N{DEGREE SIGN} F' in print_out
        assert f'Feels Like: 44.2\N{DEGREE SIGN} F' in print_out
        assert 'Last Updated: 2026-11-04 19:00' in print_out


    def test_day1_values(self, print_out):
        """Tests that the first day values are present in the print out"""
        assert 'Date: Wed, 04 Nov 2026' in print_out
        assert 'Condition: Sunny' in print_out
        assert 'High: 52.7' in print_out
        assert 'Low: 32.7' in print_out


    def test_day2_values(self, print_out):
        """Tests that the second day values are present in the print out"""
        assert 'Date: Thu, 05 Nov 2026' in print_out
        assert 'Condition: Sunny' in print_out
        assert 'High: 54.1' in print_out
        assert 'Low: 31.8' in print_out