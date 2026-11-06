# Tiffany Mui - Module 7 Assignment

A weather tool that pulls live data from weatherapi.com.

Estimated Minimum: ![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)    
Development Environment: Python 3.14.4

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modules](#modules)
- [Testing](#testing)
- [Author/Credits](#author--credits)

---

## Overview
The weather tool was created for State University of New York (SUNY): Empire State University (ESU), CSCI-3025: Python Programming course as the Module 7 assignment.

The weather tool:
- Accepts user input as a search parameter to find an area based on city or zip/postal code.
- Securely handles the API key as an environment variable
- Builds the URL for use in the API call
- Pulls in raw current and forecast weather data, parses it, then displays it in an easily digestible manner

Ground work for the following features is included, but not fully implemented:
- The file name and location of the error log is coded via variable, allowing a single location change, but still present within the code
- Number of days to generate forecast data is defined via variable, allowing a single location change, but still present within the code instead of user input
- Data parsed and displayed from Weather API is limited and could be expanded in a future release
- Building the URL for the API call is done via function, enabling potential expansion to other API calls from weatherapi.com, but not currently implemented

## Features

- Logging of detailed errors from the API instead of printing those errors to the console
- Robust error handling covering timeouts, HTTP errors, request exceptions, and malformed JSON data with graceful exits when they occur
- Reusable logging module that is file/path agnostic
- All errors are logged with a datetime object

## Installation

### Prerequisites
- Python 3.11 or higher (estimated)
- External Packages
    - requests - handles http requests and responses
    - python-dotenv - handles loading environment variables
- External APIs
    - Weather API from https://www.weatherapi.com/

### Setup Steps
1. Request an API key from https://www.weatherapi.com/ (note: this does require an account creation)
2. Download the repository from https://github.com/staramarina/CSCI-3025/tree/main/Module7
3. Verify all files are present
```
   Module7/
    ├── Mui_Logging.py           # Provides support for generating error/audit logs
    ├── Mui_M7Assignment.py      # Main program
    └── Mui_WxrHandle.py         # Module that handles API calls, environment variables, parsing and displaying data
```
4. Install requests package: (note: it is recommended to utilize a virtual environment to segment dependencies)
```
python -m pip install requests
```
5. Install python-dotenv package: 
```
python -m pip install python-dotenv
```
6. Create a .env file within the Module7 directory that includes the following
```
WEATHER_API_KEY = <your_api_key>
```
7. Ensure Python path includes the Module7 directory or run from within it.

## Usage

### Running the Program
From the Module7 directory  
```python Mui_M7Assignment.py```

### Example Interaction
```
Welcome to the Weather Tool!
Search by the city name or zip/postal code
colorado springs


Location: Colorado Springs, Colorado, United States of America
Current Condition: Clear
Current Temperature: 37.4° F
Feels Like: 31.8° F
Last Updated: 2026-11-05 20:45

Date: Thu, 05 Nov 2026
Condition: Sunny
High: 54.0° F
Low: 32.9° F

Date: Fri, 06 Nov 2026
Condition: Overcast
High: 53.4° F
Low: 33.1° F

Date: Sat, 07 Nov 2026
Condition: Sunny
High: 58.2° F
Low: 34.1° F

Date: Sun, 08 Nov 2026
Condition: Sunny
High: 63.4° F
Low: 34.0° F

Date: Mon, 09 Nov 2026
Condition: Sunny
High: 65.2° F
Low: 39.3° F

Date: Tue, 10 Nov 2026
Condition: Partly Cloudy
High: 61.1° F
Low: 36.4° F

Date: Wed, 11 Nov 2026
Condition: Partly Cloudy
High: 56.8° F
Low: 36.8° F
```

## Project Structure
```
   Module7/
    ├── Mui_Logging.py           # Provides support for generating error/audit logs
    ├── Mui_M7Assignment.py      # Main program
    ├── Mui_WxrHandle.py         # Module that handles API calls, environment variables, as well as parsing and displaying data
    ├── README.md                # Read me file (current file)
    ├── pyproject.toml           # Project configuration file
    └── tests                    # Test files for pytest
          ├── __init__.py        # Tells Python this is a package
          ├── test_logging.py    # Tests for Mui_Logging.py
          └── test_wxr.py        # Tests for Mui_WxrHandle.py
```

## Modules

### Built-in Packages
- sys for graceful program exits
- os to support pathing
- pathlib for paths to call for .env file
- copy to make deep copies without affecting original instances
- datetime for representing dates

### External Packages
- dotenv for portable handling of environment variables
- requests for handling API calls

### Logging Module (Mui_Logging.py)
| Function | Purpose | Return |
| ----- | ------ | ------ |
| can_write_file(file_name) | Checks if a file can be appended | (bool, str) - success flag, message (duplicated from Module5) |
| print_log(data, file_name) | Prints log entries to an existing file (will create if not present) | (bool, str) - success flag, message |
| err_handle(err_msg, err_log='log.txt') | Handles various errors, prints console message and calls print_log | None (console output) |

### Weather Handling Module (Mui_WxrHandle.py)
| Function | Purpose | Return |
| ----- | ------ | ------ |
| load_env() | Loads API configuration from environment variables file | The API key stored as environment variable |
| loc_parsing(raw) | Parses location input and formats it for use in the API URL | formated location string |
| build_url(api_key, location='London', days='7') | Builds the query URL for forecast portion of weather API | The URL used to query for forecast weather data |
| wxr_api_call(url, timeout=10, err_log='log.txt') | Calls the weather API | JSON data from the Weather API |
| json_parsing(data, err_log='log.txt') | Parses JSON data received from weather API to a dictionary | Parsed data including only values used by program |
| wxr_display(par) | Prints weather information to the console | None (console output only) |

## Testing

### Manual Testing
All testing with the real weather API was conducted manually to prevent excessive calls to the API. Manual testing included verifying that the API was successfully pulled from environment variables file, the call URL was built correctly, the raw data was successfully received, and the data was successfully parsed then displayed. A full end-to-end manual test was conducted with various user input to include no input. 

### Automated Testing

## Author & Credits
Author: Tiffany M. Mui  
Institution: State University of New York: Empire State University  
Course: CSCI-3025 - Python Programming  
Instructor: Dr. Sahand Ziabari  
Date: 06 Nov 2026  
