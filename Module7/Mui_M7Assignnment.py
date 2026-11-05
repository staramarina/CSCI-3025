# Tiffany M. Mui
# Module 7 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: Weather and forecast tool
# Dependencies: TBD


import Mui_WxrHandle as wxr


if __name__ == "__main__":
    err_log = 'Mui_M7_Log.txt'
    days = '7'
    timeout = 10
    #location = 'London' # TODO: implement this as input later
    location = 'Colorado+Springs' # TODO account for spaces, this is a correct query
    api_key = wxr.load_env()
    #url_cur = wxr.build_current_url(api_key, location) # Don't need this, current included with forecast
    url_for = wxr.build_forecast_url(api_key, location, days)



    url = 'https://api.weatherapi.com/v1/current.json?key=None&qLondon' # invalid url used to test HTTP error response
    data = wxr.wxr_api_call(url, timeout, err_log) # TODO: put real URLs later when ready to make real calls
    #data = wxr.wxr_api_call(url_for, timeout, err_log) # WORKS with location = 'Colorado+Springs'
    print(data)


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