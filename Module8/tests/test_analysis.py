# Tiffany M. Mui
# Module 8 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for analysis module
# Run with: pytest tests/test_analysis.py -v


import sys
from pathlib import Path
from datetime import date
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
        date: close_approach_date as a datetime object
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
        'name': 'Test NEO',
        'nasa_jpl_url': 'https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html',
        'close_approach_date_full': date,
        'orbiting_body': orbit,
        'miss_distance_kilometers': 45865643.869616206,
        'miss_distance_lunar': d_lunar,
        'relative_velocity_kilometers_per_second': 16.094142,
        'meters_estimated_diameter_max': d_max,
        'meters_estimated_diameter_min': d_min
    }
    return row


FEED_DATA = []