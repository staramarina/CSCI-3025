# Tiffany M. Mui
# Module 7 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: Weather and forecast tool
# Dependencies:
#   Standard: os, pathlib, copy, datetime
#   External: dotenv, requests
#   Custom: Mui_Logging.py, Mui_WxrHandle.py


import Mui_WxrHandle as wxr


if __name__ == "__main__":
    err_log = 'Mui_M7_Log.txt'
    days = '7'
    timeout = 10
    loc_in = 'Colorado Springs' # TODO: implement this as input later
    location = wxr.loc_parsing(loc_in)
    api_key = wxr.load_env()
    url = wxr.build_url(api_key, location, days)
    raw = wxr.wxr_api_call(url, timeout, err_log)
    data = wxr.json_parsing(raw)
    wxr.wxr_display(data)