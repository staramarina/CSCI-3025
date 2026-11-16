# Tiffany M. Mui
# Module 8 Assignment - NASA NeoWs API Handling Module
# CSCI-3025: Python Programming
# Purpose: Functions to handle interacting with the NeoWs API
# Dependencies: 
#   Standard: sys, os, pathlib, copy, datetime
#   External: dotenv, requests, pandas
#   Custom: Mui_Logging.py, Mui_Ancilly.py


import sys
import os
from pathlib import Path
from copy import deepcopy
from datetime import datetime
from dotenv import load_dotenv
import requests
import pandas as pd
from Mui_Ancillary import date_format
from Mui_Logging import err_handle


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


def build_feed_url(api_key, start, end, err_log='log.txt'):
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
    start_check = date_format(start)
    if start_check[0]:
        start_url = f'start_date={start}'
    else:
        start_url = 'start_date=2026-10-28'
        err = start_check[1] + ' Defaulted to 2026-10-28'
        err_handle(err, err_log)
    end_check = date_format(end)
    if end_check[0]:
        end_url = f'&end_date={end}'
    else:
        end_url = '&end_date=2026-10-29'
        err = end_check[1] + ' Defaulted to 2026-10-29'
        err_handle(err, err_log)
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
    base_url = 'https://api.nasa.gov/neo/rest/v1/neo/'
    id_url = f'{asteroid_id}?'
    key_url = f'api_key={api_key}'
    url = base_url + id_url + key_url
    return url


def neows_call(url, timeout=10, err_log='log.txt'): # Heavy reuse from Module 7
    """Calls the NASA NeoWs API
    
    Args:
        url: URL generated from build_feed_url or build_lookup_url
        timeout: length of time in seconds to wait for a response from the API
        err_log: the file path where the log is located
    
    Returns:
        data: JSON data from the NASA NeoWs API
    """
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        data = r.json()
    except requests.exceptions.Timeout as time_err:
        err_handle(time_err, err_log)
        sys.exit(1)
    except requests.exceptions.HTTPError as http_err:
        err_handle(http_err, err_log)
        sys.exit(1)
    except requests.exceptions.RequestException as req_err:
        err_handle(req_err, err_log)
        sys.exit(1)
    except ValueError as json_err:
        err_handle(json_err, err_log)
        sys.exit(1)
    else:
        return data


def build_dataframe(json_data):
    """Builds pandas dataframe from nested JSON data
    
    Args:
        json_data: raw nested JSON data

    Returns:
        data: pandas dataframe with close approach and nested dicts flattened
    """
    if 'near_earth_objects' in json_data:
        all_neo = []
        for neo_list in json_data['near_earth_objects'].values():
            all_neo.extend(neo_list)
        df = pd.DataFrame(all_neo)
    else:
        df = pd.DataFrame(json_data)
    df = df.explode('close_approach_data', ignore_index=True)
    cad = pd.json_normalize(df['close_approach_data'], sep='_')
    col_flat = []
    for col in df.columns:
        if ('close_approach_data' != col
                and df[col].map(type).eq(dict).any()):
            col_flat.append(col)
    frame_flat = [df.drop(columns=['close_approach_data'] + col_flat), cad]
    for col in col_flat:
        flat = pd.json_normalize(df[col], sep='_')
        frame_flat.append(flat)
    data = pd.concat(frame_flat, axis=1)
    return data


# TODO build separate data cleaning/formatting function