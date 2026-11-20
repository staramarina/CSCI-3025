# Tiffany Mui - Module 8 Assignment

Exploration of Potentially Hazardous Objects (PHOs) from NASA's Near-Earth Object Web Service (NeoWs) API (https://api.nasa.gov).

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
The NeoWs analysis was created for State University of New York (SUNY): Empire State University (ESU), CSCI-3025: Python Programming course as the Module 8 assignment.

The NeoWs analysis: 
- Pulls JSON data from the feed and lookup endpoints of NASA's NeoWs API.
- Loads JSON data into pandas dataframes
- Trims superfluous data
- Cleans data to ensure that missing values are consistently marked and converts from strings to expected datatypes (e.g. float, int, datetime)
- Copies the dataframe and performs analysis objective trimming (e.g. all unused columns are removed) - this is done per analysis (in the analysis module) and leaves the original data alone
- Performs statistical calculations based on analysis objective - this is done per analysis (in the analysis module)
- Generates charts using matplotlib and seaborn - this is done per analysis (in the analysis module)
- Saves charts to a separate charts folder for clean directories

Ground work for the following features is included, but not fully implemented:
- NeoWs lookup endpoint is fully fleshed out, but main program hard-codes Didymos for this specific analysis
- NeoWs feed endpoint is fully fleshed out, but main program hard-codes analysis dates for consistent analysis
- General API handling with data trimming/cleanup is performed separately than the analysis trimming/cleanup
    - Allows reuse of NeoWs Handle module for other analysis objectives, simply replace the Analysis module and place calls in the main program for it.
    - Trimmed common columns in NeoWs Handle module were conducted for security related (exposing API key), conversions (miles, kilometers), or near duplicate data (close approach date vs. close approach date full)
    - Trimmed lookup data in NeoWs Handle was done for brevity, but ensured enough data points to fully plot the orbit

## Features

- Logging of detailed errors from the API instead of printing those errors to the console
- Robust error handling covering timeouts, HTTP errors, request exceptions, and malformed JSON data with graceful exits when they occur
- Reusable logging module that is file/path agnostic
- All errors are logged with a datetime object
- Reusable ancillary module for general purpose helper and data checking functions
- Analysis agnostic NASA NeoWs API handling module

## Installation

### Prerequisites
- Python 3.11 or higher (estimated)
- External Packages
    - requests - handles http requests and responses
    - python-dotenv - handles loading environment variables
    - pandas - handles data formatting and analysis
    - seaborn - creates graphs
    - matplotlib - handles the underlying settings for graphs
- External APIs
    - NASA NeoWs API from https://api.nasa.gov

### Setup Steps
1. Request an API key from https://api.nasa.gov (a demo key is available, but rates are limited)
2. Download the repository from https://github.com/staramarina/CSCI-3025/tree/main/Module8
3. Verify all files and folders are present
```
   Module8/
    ├── charts                          # Empty directory to hold generated charts
    ├── Mui_Analysis.py                 # Specific analysis functions, including data trimming/cleaning
    ├── Mui_Ancillary.py                # General purpose ancillary tools
    ├── Mui_Logging.py                  # Provides support for generating error/audit logs
    ├── Mui_M8Assignment.py             # Main program
    └── Mui_NeoWsHandle.py              # Handles API calls, environment variables, as well as general data trimming/cleaning
```
4. Install python-dotenv package: (note: it is recommended to utilize a virtual environment to segment dependencies)
```
python -m pip install python-dotenv
```
5. Install requests package:
```
python -m pip install requests
```
6. Install pandas package:
```
python -m pip install pandas
```
7. Install seaborn package: (note: this includes matplotlib installation)
```
python -m pip install seaborn
```
8. Create a .env file within the Module8 directory that includes the following
```
API_KEY = <your_api_key>
```
9. Ensure Python path includes the Module8 directory or run from within it.

## Usage

### Running the Program
From the Module8 directory  
```python Mui_M8Assignment.py```

### Example Interaction
```
Let's explore Near-Earth Objects!

Pulling feed data from 2026-11-08 to 2026-11-14..... Done!
Trimming feed data..... Done!
Cleaning feed data..... Done!
Pulling lookup data on Didymos..... Done!
Trimming Didymos data..... Done!
Cleaning Didymos data..... Done!
Cleaning, analyzing, and plotting PHO vs. non-PHO per day with average statistics..... Done!
Cleaning, analyzing, and plotting miss distance per day with average statistics..... Done!
Cleaning, analyzing, and plotting PHO minimum and maximum diameter per day with Didymos comparison points..... Done!
Cleaning, analyzing, and plotting Didymos orbiting patterns for Earth and Mars with comparison against DART impact..... Done!
Saving PHO vs. non-PHO chart..... Done!
Saving miss distance chart..... Done!
Saving PHO diameter comparison chart..... Done!
Saving Didymos orbit patterns chart..... Done!

All tasks complete!
Charts are located in the charts folder.
```

### Generated Charts

![chart of PHO vs. non-PHO per Day with Average Statistics](charts/neo_chart.png)

![chart of Miss distance per Day with Average Statistics](charts/lun_chart.png)

![chart of PHO Minimum and Maximum Diameter per Day with Didymos Comparison Points](charts/pho_chart.png)

![chart of Didymos Orbiting Patterns for Earth and Mars with Comparison against DART Impact](charts/didymos_chart.png)

## Project Structure
```
   Module8/
    ├── Mui_Analysis.py                 # Specific analysis functions, including data trimming/cleaning
    ├── Mui_Ancillary.py                # General purpose ancillary tools
    ├── Mui_Logging.py                  # Provides support for generating error/audit logs
    ├── Mui_M8Assignment.py             # Main program
    ├── Mui_NeoWsHandle.py              # Handles API calls, environment variables, as well as general data trimming/cleaning
    ├── pyproject.toml                  # Project configuration file
    ├── README.md                       # Read me file (current file)
    ├── charts                          # Directory to hold generated charts
    │     ├── didymos_chart.png         # Chart from Didymos orbiting patterns for Earth and Mars with comparison against DART impact
    │     ├── lun_chart.png             # Chart from miss distance per day with average statistics analysis
    │     ├── neo_chart.png             # Chart from PHO vs. non-PHO per day with average statistics analysis
    │     └── pho_chart.png             # Chart from PHO minimum and maximum diameter per day with Didymos comparison points
    ├── tests                           # Test files for pytest
    │     ├── __init__.py               # Tells Python this is a package
    │     ├── test_analysis.py          # Tests for Mui_Analysis.py
    │     ├── test_ancillary.py         # Tests for Mui_Ancillary.py
    │     └── test_neows.py             # Tests for Mui_NeoWsHandle.py
    └── exampledata                     # Data used for manual tests
          ├── didymos_sampledata.txt    # Real lookup endpoint output data
          ├── feed_sampledata.txt       # Real feed endpoint output data
          └── test_dump.txt             # A dump of the analysis data used for testing purposes
```

## Modules

### Built-in Packages
- sys for graceful program exits
- os to support pathing
- pathlib for paths to call for .env file
- copy to make shallow copies without affecting original instances
- datetime for representing dates

### External Packages
- dotenv for portable handling of environment variables
    - Estimated Minimum: 1.0
    - Development Environment: 1.2.4
- requests for handling API calls
    - Estimated Minimum: 2.31
    - Development Environment: 2.34.2
- pandas for handling large data formatting and analysis
    - Estimated Minimum: 2.0
    - Development Environment: 3.1.1
- seaborn for creating graphs
    - Estimated Minimum: 0.13
    - Development Environment: 0.13.2
- matplotlib for handling graph input
    - Estimated Minimum: 3.7
    - Development Environment: 3.11.2

### Analysis Module (Mui_Analysis.py)
| Function | Purpose | Return |
| ----- | ------ | ------ |
| neo_pho_trim(data) | Trims data for analysis and plotting of PHO vs. non-PHO per day with comparing averages | trimmed dataframe with only close_approach_date_full and is_potentially_hazardous_asteroid values, with missing values removed |
| neo_avg_calc(trim) | Calculates average PHO statistics | A 3-tuple of the format (average non-PHO, average PHO, average NEO)|
| neo_pho_chart(data) | Generates a clustered column chart of PHO/non-PHO per day with average comparison lines | A 2-tuple of the format (matplotlib figure, matplotlib axes) |
| lun_miss_trim(data) | Trims data for analysis and plotting of lunar miss distance per day with comparing averages | trimmed dataframe with only close_approach_date_full and miss_distance_lunar values, with missing values removed |
| lun_miss_chart(data) | Generates box-and-whisker chart of lunar miss distance per day | A 2-tuple of the format (matplotlib figure, matplotlib axes) |
| pho_size_trim(data) | Trims data for analysis and plotting of min/max diameter of PHO per day with comparison against Didymos | long format trimmed dataframe with min/max and estimated diameter columns of only PHOs with missing values removed |
| pho_size_chart(data, didymos_data) | Generates bar chart of diameters of all PHOs per day, with comparison against Didymos | A 2-tuple of the format (matplotlib figure, matplotlib axes) |
| didymos_orbit_trim(data) | Trims data for analysis and plotting of Didymos orbiting patterns | trimmed dataframe with only close_approach_date_full, miss_distance_lunar, and orbiting_body values, with missing values removed |
| didymos_orbit_chart(data) | Generates a line plot of Didymos miss distance by flyby body | A 2-tuple of the format (matplotlib figure, matplotlib axes) |

### Ancillary Module (Mui_Ancillary.py)
| Function | Purpose | Return |
| ----- | ------ | ------ |
| dtg_check(date_str, format_str) | Determines whether a string can be converted to a datetime object | (True, datetime object) if successful, otherwise (False, error message) |
| chart_save(chart, file_name, dpi=150) | Saves a chart as an image file | A 2-tuple with True/False success flag and additional information |

### Logging Module (Mui_Logging.py)
Note: This module is largely unchanged from Module 7, included again here for completness.
| Function | Purpose | Return |
| ----- | ------ | ------ |
| can_write_file(file_name) | Checks if a file can be appended | (bool, str) - success flag, message (duplicated from Module5) |
| print_log(data, file_name) | Prints log entries to an existing file (will create if not present) | (bool, str) - success flag, message (duplicated from Module7) |
| err_handle(err_msg, err_log='log.txt') | Handles various errors, prints console message and calls print_log | None (console output) (heavy reuse from Module7) |

### NeoWs Handle Module (Mui_NeoWsHandle.py)
| Function | Purpose | Return |
| ----- | ------ | ------ |
| load_env() | Loads API configuration from environment variables file | The API key stored as environment variable (reused from Module7) |
| build_feed_url(api_key, start, end, err_log="log.txt") | Builds the Neo-Feed query URL | The URL used to query for asteroids based on closest approach date |
| build_lookup_url | Builds the Neo-Lookup query URL | The URL used to query for specific asteroid data |
| neows_call(url, timeout=10, err_log="log.txt") | Calls the NASA NeoWs API | JSON data from the NASA NeoWs API (exits with error and logs) |
| build_dataframe(json_data) | Builds pandas dataframe from nested JSON data | pandas dataframe with close approach and nested dicts flattened |
| trim_common_data(data) | Removes unused columns from feed or lookup dataframe | trimmed feed/lookup data with unused columns removed |
| trim_lookup_data(data) | Removes unused columns that only appear in the lookup dataframe | trimmed lookup data with unused columns removed |
| clean_common_data(data_raw) | Handles common missing or malformed data within a dataframe | feed/lookup data with values in expected formats |
| clean_lookup_data(data_raw) | Handles lookup specific missing or malformed data within a dataframe | lookup data with values in expected formats |

## Testing

### Manual Testing
All testing with NASA's NeoWs API was conducted manually to prevent excessive calls to the API. Manual testing included verifying that the API was successfully pulled from environment variables file, the call URL was built correctly, the raw data was successfully received, and the data was successfully inserted into pandas dataframes. A full end-to-end manual test was conducted with various user input to include no input. 

Data output was visually inspected within a file using the following code within the main program to dump the data to a text file. 
```
   with open('exampledata/test_dump.txt', "a") as f:
        f.write(feed_data_clean.to_string(header=True, index=True)) # dumps data from feed endpoint
        f.write('\n\n') # extra lines for readability
        f.write(lookup_data_clean.to_string(header=True, index=True)) # dumps data from lookup endpoint
```

### Automated Testing
Automated testing was conducted with pytest. All API calls are mocked instead of calling the real API, thus all tests can be run with a dummy API key. To run the test, enter the following from within the Module8 directory.
```
python -m pytest
```

#### NeoWs Handle Module Tests (test_neows.py)

##### Testing Fixtures, Variables, and Functions
| Type | Name | Purpose |
| ----- | ------ | ------ |
TODO

##### Testing Classes & Methods
| Class | Method | Purpose |
| ----- | ------ | ------ |

## Author & Credits
Author: Tiffany M. Mui  
Institution: State University of New York: Empire State University  
Course: CSCI-3025 - Python Programming  
Instructor: Dr. Sahand Ziabari  
Date: XX Nov 2026  
