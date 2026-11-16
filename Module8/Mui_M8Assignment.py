# Tiffany M. Mui
# Module 8 Assignment - Main Program
# CSCI-3025: Python Programming
# Purpose: NASA NeoWs Exploration
# Dependencies:
#   Standard: TBD
#   External: TBD
#   Custom: TBD


import Mui_NeoWsHandle as neows


if __name__ == "__main__":
    err_log = 'Mui_M8_Log.txt'
    timeout = 10
    print('\nLet\'s explore Near-Earth Objects!')
    api_key = neows.load_env()
    start = '2026-11-01' # TODO: Change this to user input later
    end = '2026-11-03' # TODO: Change this to user input later
    url = neows.build_feed_url(api_key, start, end, err_log)
    data = neows.neows_call(url, timeout, err_log)
    print(data) # TODO: Test line, remove later