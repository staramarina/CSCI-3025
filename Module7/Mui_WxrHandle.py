# Tiffany M. Mui
# Module 7 Assignment - Weather API Handling Module
# CSCI-3025: Python Programming
# Purpose: Functions to handle interacting with the Weather API
# Dependencies: 
#   Standard: sys, os, pathlib, copy, datetime
#   External: dotenv, requests 
#   Custom: Mui_Logging.py


import sys
import os
from pathlib import Path
from copy import deepcopy
from datetime import datetime
from dotenv import load_dotenv
import requests
from Mui_Logging import err_handle


def load_env():
    """Loads API configuration from environment variables file
    
    Args:
        None
    
    Returns:
        api_key
    """
    load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")
    api_key = os.getenv("WEATHER_API_KEY")
    return api_key


def loc_parsing(raw):
    """Parses location input and formats it for use in the API URL
    
    Args:
        raw: unformated city, zip/postal code of the desired weather data
    
    Returns:
        loc: formated location string
    """
    raw = str(raw)
    raw = raw.strip()
    raw = raw.title()
    loc = raw.replace(' ', '+')
    return loc


def build_url(api_key, location='London', days='7'):
    """Builds the query URL for forecast portion of weather API
    
    Args:
        api_key: The API key that was returned from load_env()
        location: city, zip/postal code of the desired weather data
    
    Returns:
        url: The URL used to query for forecast weather data
        e.g.: https://api.weatherapi.com/v1/forecast.json?key=KEY&q07112&days=7
    """
    base_url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q="
    day_url = "&days="
    url = base_url + str(location) + day_url + str(days)
    return url


def wxr_api_call(url, timeout=10, err_log='log.txt'):
    """Calls the weather API
    
    Args:
        url: URL generated from either build_current_url or build_forecast_url
        timeout: length of time in seconds to wait for a response from the API
    
    Returns:
        data: JSON data from the Weather API
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


def json_parsing(data, err_log='log.txt'):
    """Parses JSON data received from weather API to a dictionary
    
    Args:
        data: raw JSON data received from the weather API
    
    Returns:
        par: parsed data including only values used by program
    """
    try:
        par = {
            'name': data["location"]["name"],
            'region': data["location"]["region"],
            'country': data["location"]["country"],
            'last': data["current"]["last_updated"],
            'temp_now': data["current"]["temp_f"],
            'feels': data["current"]["feelslike_f"],
            'con_text': data["current"]["condition"]["text"],
        }
        for dtg in data["forecast"]["forecastday"]:
            this_date = dtg["date"]
            max_t = dtg["day"]["maxtemp_f"]
            min_t = dtg["day"]["mintemp_f"]
            con = dtg["day"]["condition"]["text"]
            par[this_date] = [max_t, min_t, con]
    except KeyError as key_err:
        err_handle(key_err, err_log)
        sys.exit(1)
    else:
        return par


def wxr_display(par):
    """Prints weather information to the console
    
    Args:
        data: parsed data from json_parsing(data)
    
    Returns:
        None (Console output only)
    """
    data = deepcopy(par)
    city = data.pop('name')
    state = data.pop('region')
    country = data.pop('country')
    last = data.pop('last')
    temp_now = data.pop('temp_now')
    feels = data.pop('feels')
    con_text = data.pop('con_text')
    print('\n')
    print(f'Location: {city}, {state}, {country}')
    print(f'Current Condition: {con_text}')
    print(f'Current Temperature: {temp_now}\N{DEGREE SIGN} F')
    print(f'Feels Like: {feels}\N{DEGREE SIGN} F')
    print(f'Last Updated: {last}\n')
    for key, value in data.items():
        day_comp = key.split('-')
        year = int(day_comp[0])
        month = int(day_comp[1])
        day = int(day_comp[2])
        date = datetime(year, month, day)
        print(f'Date: {date.strftime("%a, %d %b %Y")}')
        max_t = value[0]
        min_t = value[1]
        con = value[2]
        print(f'Condition: {con}')
        print(f'High: {max_t}\N{DEGREE SIGN} F')
        print(f'Low: {min_t}\N{DEGREE SIGN} F\n')