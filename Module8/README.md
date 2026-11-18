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
TBD

## Features

- TBD

## Installation

### Prerequisites
- Python 3.11 or higher (estimated)
- External Packages
    - requests - handles http requests and responses (estimated minimum: 2.31, dev/test environment: 2.34.2)
    - python-dotenv - handles loading environment variables (estimated minimum: 1.0, dev/test environment: 1.2.4)
    - pandas - handles data formatting and analysis (estimated minimum: 1.1, dev/test environment: 3.1.1)
- External APIs
    - NASA NeoWs API from https://api.nasa.gov

### Setup Steps
1. Request an API key from https://api.nasa.gov
2. Download the repository from https://github.com/staramarina/CSCI-3025/tree/main/Module8
3. Verify all files are present
```
TBD
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
7. Create a .env file within the Module8 directory that includes the following
```
API_KEY = <your_api_key>
```
8. Ensure Python path includes the Module8 directory or run from within it.

## Usage

### Running the Program
From the Module8 directory  
```python Mui_M8Assignment.py```

### Example Interaction
```
TBD
```

## Project Structure
```
   Module8/
    ├── Mui_M8Assignment.py      # Main program
    ├── README.md                # Read me file (current file)
    ├── pyproject.toml           # Project configuration file
    └── TBD
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
    - Estimated Minimum: 1.1
    - Development Environment: 3.1.1

### Custom Modules
TODO

## Testing

### Manual Testing
All testing with NASA's NeoWs API was conducted manually to prevent excessive calls to the API. Manual testing included verifying that the API was successfully pulled from environment variables file, the call URL was built correctly, the raw data was successfully received, and the data was successfully inserted into pandas dataframes. A full end-to-end manual test was conducted with various user input to include no input. 

Data output was visually inspected within a file using the following code within the main program to dump the data to a text file. 
```
   with open('temp_dump.txt', "a") as f:
        f.write(feed_data_clean.to_string(header=True, index=True)) # dumps data from feed endpoint
        f.write('\n\n') # extra lines for readability
        f.write(lookup_data_clean.to_string(header=True, index=True)) # dumps data from lookup endpoint
```

### Automated Testing
TODO

## Author & Credits
Author: Tiffany M. Mui  
Institution: State University of New York: Empire State University  
Course: CSCI-3025 - Python Programming  
Instructor: Dr. Sahand Ziabari  
Date: XX Nov 2026  
