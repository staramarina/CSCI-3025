# Tiffany M. Mui
# Module 8 Assignment - NASA NeoWs API Handling Module
# CSCI-3025: Python Programming
# Purpose: Functions to handle interacting with the NeoWs API
# Dependencies: 
#   Standard: sys, os, pathlib, copy, datetime
#   External: dotenv, requests 
#   Custom: TBD


import sys
import os
from pathlib import Path
from dotenv import load_dotenv


def load_env(): # Reused from Module 7
    """Loads API configuration from environment variables file
    
    Args:
        None
    
    Returns:
        api_key: The API key stored as environment variable
    """
    load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")
    api_key = os.getenv("API_KEY")
    return api_key


def build_feed_url(api_key, start, end):
    """Builds the Neo-Feed query URL
    
    Args:
        api_key: The API key that was returned from load_env()
        start: Start date in format YYYY-MM-DD
        end: End date in format YYYY-MM-DD
    
    Returns:
        url: The URL used to query for asteroids based on closest approach date
        e.g.: https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY
    """
    base_url = 'https://api.nasa.gov/neo/rest/v1/feed?'
    start_url = f'start_date={start}'
    end_url = f'&end_date={end}'
    key_url = f'&api_key={api_key}'
    url = base_url + start_url + end_url + key_url
    return url


def build_lookup_url(api_key, asteroid_id):
    """Builds the Neo-Lookup query URL
    
    Args:
        api_key: The API key that was returned from load_env()
        asteroid_id: Asteroid SPK-ID correlates to the NASA JPL small body
    
    Returns:
        url: The URL used to query for specific asteroid data
        e.g.: https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=DEMO_KEY
    """
    base_url = 'https://api.nasa.gov/neo/rest/v1/neo'
    id_url = f'{asteroid_id}?'
    key_url = f'api_key={api_key}'
    url = base_url + id_url + key_url
    return url