# Tiffany M. Mui
# Module 7 Assignment
# CSCI-3025: Python Programming
# Purpose: Weather and forecast tool
# Dependencies: TBD


import os
import requests
import logging
from pathlib import Path
from dotenv import load_dotenv


# Load environment variables
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")


api_key = os.getenv("WEATHER_API_KEY")
base_url = "https://api.weatherapi.com/v1/" # base url for all requests
current_url = "current.json?" # gets current weather
forecast_url = "forecast.json?" # gets forecast weather up to 14 days
alert_url = "alerts.json?" # gets any active alerts (might already be included in forecast with alerts=yes)
key_url = f"key={api_key}" # url component with the api key
q_url = "&q="
day_url = "&days=7"
# Example: https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&qLondon # gets current weather in london
# Example: https://api.weatherapi.com/v1/forecast.json?key=YOUR_API_KEY&q07112&days=7 # gets weather for the next 7 days at zip 07112

location = 'London' # TODO: implement this as input later

query_url_cur = base_url + current_url + key_url + q_url + location
query_url_for = base_url + forecast_url + key_url + q_url + location + day_url


url = 'https://api.weatherapi.com/v1/current.json?key=None&qLondon' # invalid url used to test HTTP error response


try:
    r = requests.get(url, timeout=10) # TODO: update later with proper urls
    r.raise_for_status()
    data = r.json()
except requests.exceptions.Timeout:
    print('ERROR: The request timed out.')
except requests.exceptions.HTTPError as http_err: # TODO handle different statuses so API key isn't revealed.
    print('ERROR: An HTTP error occurred')
except requests.exceptions.RequestException as req_err:
    print('ERROR: A request exception occured.')
    print(req_err)
except ValueError as json_err:
    print('ERROR: Failed to decode JSON')
    print(json_err)

"""
# Example attempt -- WORKS!
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q=London"
r = requests.get(url, timeout=10)
r.raise_for_status()
data = r.json()
print(data)
"""

"""
What this printed: 
{'location': {'name': 'London', 'region': 'City of London, Greater London', 'country': 'United Kingdom', 'lat': 51.5171, 'lon': -0.1062, 'tz_id': 'Europe/London', 'localtime_epoch': 1793667898, 'localtime': '2026-11-03 01:04'}, 'current': {'last_updated_epoch': 1793667600, 'last_updated': '2026-11-03 01:00', 'temp_c': 10.9, 'temp_f': 51.6, 'is_day': 0, 'condition': {'text': 'Overcast', 'icon': '//cdn.weatherapi.com/weather/64x64/night/122.png', 'code': 1009}, 'wind_mph': 11.9, 'wind_kph': 19.1, 'wind_degree': 32, 'wind_dir': 'NNE', 'pressure_mb': 1034.0, 'pressure_in': 30.53, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 56, 'cloud': 100, 'feelslike_c': 7.5, 'feelslike_f': 45.5, 'windchill_c': 8.6, 'windchill_f': 47.5, 'heatindex_c': 10.9, 'heatindex_f': 51.6, 'dewpoint_c': 2.4, 'dewpoint_f': 36.3, 'vis_km': 10.0, 'vis_miles': 6.0, 'uv': 0.0, 'gust_mph': 22.2, 'gust_kph': 35.7, 'will_it_rain': 0, 'chance_of_rain': 13, 'will_it_snow': 0, 'chance_of_snow': 0, 'wetbulb_c': 6.9, 'wetbulb_f': 44.5, 'short_rad': 0, 'diff_rad': 0, 'dni': 0, 'gti': 0}}
"""