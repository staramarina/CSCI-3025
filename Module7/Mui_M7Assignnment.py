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
    location = 'London' # TODO: implement this as input later
    api_key = wxr.load_env()
    url_for = wxr.build_url(api_key, location, days)

    
    url = 'https://api.weatherapi.com/v1/current.json?key=None&qLondon' # invalid url used to test HTTP error response remove later
    data = wxr.wxr_api_call(url, timeout, err_log) # TODO: put real URLs later when ready to make real calls
