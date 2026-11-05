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