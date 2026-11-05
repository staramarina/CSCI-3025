# Tiffany M. Mui
# Module 7 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Shared text fixtures to provide reusable test data


import pytest
from unittest.mock import MagicMock


@pytest.fixture
def sample_data():
    """Returns sample data of the same format as a real forecast API call"""
    data = {
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


@pytest.fixture
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