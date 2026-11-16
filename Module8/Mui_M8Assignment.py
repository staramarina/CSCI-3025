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
    api_key = neows.load_env()
    print(api_key)