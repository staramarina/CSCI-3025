# Tiffany M. Mui
# Module 8 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for analysis module
# Run with: pytest tests/test_analysis.py -v


import sys
from pathlib import Path
from datetime import date, datetime
import pytest
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


import Mui_Analysis as analysis


def make_common_row(neo_id, date, pho, d_lunar, d_min, d_max, 
                    orbit='Earth'):
    """Builds a row that mimicks the output of clean_common_data
    
    Args:
        neo_id: id (SPK-ID) as a number
        date: close_approach_date as a string of 'YYY-MM-DD HH:MM'
        pho: is_potentially_hazardous_object boolean value
        d_lunar: miss_distance_lunar as a number
        d_min: meters_estimated_diameter_min as a number
        d_max: meters_estimated_diameter_max as a number
        orbit: orbiting_body as a string (default Earth)
    
    Returns:
        row: dict of one cleaned NEO observation
    """
    row = {
        'absolute_magnitude_h': 18.1,
        'id': neo_id,
        'is_potentially_hazardous_asteroid': pho,
        'name': f'Test {neo_id}',
        'nasa_jpl_url': 'https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html',
        'close_approach_date_full': pd.Timestamp(date),
        'orbiting_body': orbit,
        'miss_distance_kilometers': 45865643.869616206,
        'miss_distance_lunar': d_lunar,
        'relative_velocity_kilometers_per_second': 16.094142,
        'meters_estimated_diameter_max': d_max,
        'meters_estimated_diameter_min': d_min
    }
    return row


FEED_DATA = [
    make_common_row(
        1001, '2026-11-01 00:20', False,
        119.264636, 513.517179, 1148.259319
    ),
    make_common_row(
        1002, '2026-11-01 02:13', True,
        24.183183, 192.555078, 430.566244
    ),
    make_common_row(
        1003, '2026-11-01 12:46', False,
        118.764718, 30.517923, 68.240151
    ),
    make_common_row(
        1004, '2026-11-01 02:13', True,
        24.183388, 188.171989, 420.765360
    ),
    make_common_row( # is PHO and lunar distance missing data, expect all drop
        1005, '2026-11-03 07:03', None, 
        None, 13.631856, 30.481756
    ),
    make_common_row(
        1006, '2026-11-02 19:10', False,
        179.038968, 205.378500, 459.240286
    ),
    make_common_row( # missing min diameter data, expect drop at pho_size_trim
        1007, '2026-11-02 21:35', True,
        67.962402, None, 25.353620
    ),
    make_common_row(
        1008, '2026-11-02 17:55', True,
        15.649873, 69.912523, 156.329154
    ),
    make_common_row(
        1009, '2026-11-02 20:00', False,
        140.499671, 63.760979, 142.573883
    ),
]
ORBIT_DATA = [
    {
        'close_approach_date_full': pd.Timestamp('1901-02-04 17:18:00'),
        'miss_distance_lunar': 20.287754,
        'orbiting_body': 'Mars'
    }, {
        'close_approach_date_full': pd.Timestamp('1967-10-08 21:37'),
        'miss_distance_lunar': 20.783773,
        'orbiting_body': 'Mars'
    }, {
        'close_approach_date_full': pd.Timestamp('2022-10-04 09:48'),
        'miss_distance_lunar': 27.709694,
        'orbiting_body': 'Earth'
    }, { 
        'close_approach_date_full': pd.Timestamp('2083-11-29 13:12'),
        'miss_distance_lunar': None, # missing, expect dropped
        'orbiting_body': 'Earth'
    }, {
        'close_approach_date_full': pd.Timestamp('2144-07-31 12:02'),
        'miss_distance_lunar': 12.181374,
        'orbiting_body': 'Mars'
    }, {
        'close_approach_date_full': pd.Timestamp('2144-12-02 23:10'),
        'miss_distance_lunar': 69.311856,
        'orbiting_body': 'Earth'
    }, {
        'close_approach_date_full': pd.Timestamp('2184-10-14 10:11'),
        'miss_distance_lunar': 22.333426,
        'orbiting_body': 'Earth'
    }
]
DIDYMOS_MIN = 634.680239
DIDYMOS_MAX = 1419.188158