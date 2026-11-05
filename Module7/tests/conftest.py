# Tiffany M. Mui
# Module 7 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Shared text fixtures to provide reusable test data


import pytest


@pytest.fixture
def bad_key():
    """Returns a URL with an invalid key"""
    bad_key_url = 'https://api.weatherapi.com/v1/current.json?key=None&qLondon'
    return bad_key_url


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