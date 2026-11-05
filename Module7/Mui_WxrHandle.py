# Tiffany M. Mui
# Module 7 Assignment - Weather API Handling Module
# CSCI-3025: Python Programming
# Purpose: Functions to handle interacting with the Weather API
# Dependencies: TBD


import os
from pathlib import Path
from dotenv import load_dotenv
import requests
from Mui_Logging import print_log


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


def build_current_url(api_key, location):
    """Builds the query URL for current portion of weather API
    
    Args:
        api_key: The API key that was returned from load_env()
        location: city, zip/postal code of the desired weather data
    
    Returns:
        url: The URL used to query for current weather data
        e.g.: https://api.weatherapi.com/v1/current.json?key=KEY&qLondon
    """
    base_url = "https://api.weatherapi.com/v1/"
    current_url = "current.json?"
    key_url = f"key={api_key}&q="
    url = base_url + current_url + key_url + str(location)
    return url


def build_forecast_url(api_key, location, days):
    """Builds the query URL for forecast portion of weather API
    
    Args:
        api_key: The API key that was returned from load_env()
        location: city, zip/postal code of the desired weather data
    
    Returns:
        url: The URL used to query for forecast weather data
        e.g.: https://api.weatherapi.com/v1/forecast.json?key=KEY&q07112&days=7
    """
    base_url = "https://api.weatherapi.com/v1/"
    forecast_url = "forecast.json?"
    key_url = f"key={api_key}&q="
    day_url = "&days="
    url = (base_url + forecast_url + key_url + str(location) 
           + day_url + str(days))
    return url


def wxr_api_call(url, timeout=10, err_log='log.txt'):
    """Calls the weather API
    
    Args:
        url: URL generated from either build_current_url or build_forecast_url
        timeout: length of time in seconds to wait for a response from the API
    
    Returns:
        data: JSON data from the Weather API
    """
    print(url) # test line remove later
    std_err = 'ERROR: An error occurred with the Weather API.'
    see_log = f'See {err_log} for details.'
    log_err = 'Could not send error to the logs:'
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        data = r.json()
    except requests.exceptions.Timeout:
        print('ERROR: The request timed out.')
    except requests.exceptions.HTTPError as http_err:
        flag = print_log(http_err, err_log)
        if flag[0]:
            print(f'{std_err} {see_log}')
        else:
            print(f'{std_err}')
            print(f'{log_err} {flag[1]}')
    except requests.exceptions.RequestException as req_err:
        flag = print_log(req_err, err_log)
        if flag[0]:
            print(f'{std_err} {see_log}')
        else:
            print(f'{std_err}')
            print(f'{log_err}  {flag[1]}')
    except ValueError as json_err:
        flag = print_log(json_err, err_log)
        if flag[0]:
            print(f'{std_err} {see_log}')
        else:
            print(f'{std_err}')
            print(f'{log_err}  {flag[1]}')
    else:
        return data