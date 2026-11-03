# Tiffany M. Mui
# Module 7 Assignment
# CSCI-3025: Python Programming
# Purpose: Weather and forecast tool
# Dependencies: TBD


import os
import requests
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
q_url = "&q"
day_url = "&days=7"
# Example: https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&qLondon # gets current weather in london
# Example: https://api.weatherapi.com/v1/forecast.json?key=YOUR_API_KEY&q07112&days=7 # gets weather for the next 7 days at zip 07112





# Example attempt
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&qLondon"
r = requests.get(url, timeout=10)
r.raise_for_status()
data = r.json()
print(data)
