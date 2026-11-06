# Tiffany M. Mui
# Module 7 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: Weather and forecast tool
# Dependencies:
#   Standard: os, pathlib, datetime
#   External: dotenv, requests
#   Custom: Mui_Logging.py, Mui_WxrHandle.py

import Mui_WxrHandle as wxr


SAMPLE_DATA = {
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


if __name__ == "__main__":
    err_log = 'Mui_M7_Log.txt'
    days = '7'
    timeout = 10
    loc_in = 'London' # TODO: implement this as input later
    location = wxr.loc_parsing(loc_in)
    api_key = wxr.load_env()
    url_for = wxr.build_url(api_key, location, days)



    #testing parsing data from sample to avoid repeated API calls
    data = wxr.json_parsing(SAMPLE_DATA)
    print(data)
    print('\n')
    wxr.wxr_display(data)
    #data = json.dumps(SAMPLE_DATA)
    #print(data)

    
    #url = 'https://api.weatherapi.com/v1/current.json?key=None&qLondon' # invalid url used to test HTTP error response remove later
    #data = wxr.wxr_api_call(url, timeout, err_log) # TODO: put real URLs later when ready to make real calls
