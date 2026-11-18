# Tiffany M. Mui
# Module 8 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for NeoWs Handle module
# Run with: pytest tests/test_neows.py -v


import sys
from pathlib import Path
from copy import deepcopy
import pytest
from unittest.mock import patch, MagicMock
import requests
import pandas as pd


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


import Mui_NeoWsHandle as neows


def make_cad(date, d_lun, v_kms):
    """Builds sample close_approach_data
    
    Args:
        date: the close approach date
        d_lun: miss_distance in lunar
        v_kms: relative_velocity in km/s
    
    Returns:
        cad: a single cad entry for the cad list
    """
    cad = {
        'close_approach_date': date,
		'close_approach_date_full': '2026-Nov-01 00:20', 
		'epoch_date_close_approach': 1793492400000, 
		'miss_distance': {
			'astronomical': '0.3065928938', 
			'kilometers': '45865643.869616206', 
			'lunar': d_lun, 
			'miles': '28499589.5570514028'
		},
		'orbiting_body': 'Earth', 
		'relative_velocity': {
		    'kilometers_per_hour': '57938.9128152772', 
			'kilometers_per_second': v_kms, 
			'miles_per_hour': '36000.9872434704'
        }
    }
    return cad


def make_neo(neo_id, name, cad_ls):
    """Builds a sample Near-Earth Object entry
    
    Args:
        neo_id: SPK-ID of the NEO
        name: name of the NEO
        cad_ls: list of close_approach_data
    
    Returns:
        neo: a single neo entry
    """
    neo = {
        'absolute_magnitude_h': 18.57,
        'close_approach_data': cad_ls,
        'estimated_diameter': {
			'feet': {
				'estimated_diameter_max': 3767.2551044911, 
				'estimated_diameter_min': 1684.767700445
			}, 
			'kilometers': {
				'estimated_diameter_max': 1.1482593191, 
				'estimated_diameter_min': 0.5135171787
			}, 
			'meters': {
				'estimated_diameter_max': 1148.2593191046, 
				'estimated_diameter_min': 513.5171786631
			}, 
			'miles': {
				'estimated_diameter_max': 0.7134950414, 
				'estimated_diameter_min': 0.3190846828
			}
		}, 
		'id': neo_id, 
		'is_potentially_hazardous_asteroid': False, 
		'is_sentry_object': False, 
		'links': {
			'self': 'http://api.nasa.gov/neo/rest/v1/neo/'
		}, 
		'name': name, 
		'nasa_jpl_url': 'https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html', 
		'neo_reference_id': neo_id
    }
    return neo


FEED_JSON = {
    'element_count': 16, 
    'links': {
		'next': 'http://api.nasa.gov/neo/rest/v1/feed?start_date=2026-11-03', 
		'previous': 'http://api.nasa.gov/neo/rest/v1/feed?start_date=2026-10-30', 
		'self': 'http://api.nasa.gov/neo/rest/v1/feed?start_date=2026-11-01'
    },
    'near_earth_objects': {
        '2026-11-01': [
            {make_neo('1001', 'Test A', [
                make_cad('2026-11-01', '119.2646356882', '16.0941424487')
            ])},
            {make_neo('1002', 'Test B', [
                make_cad('2026-11-01', '118.7647184455', '4.6212629351')
            ])}
        ],
        '2026-11-02': [
            {make_neo('1003', 'Test C', [
                make_cad('2026-11-02', '24.1831825905', '12.6714610504')
            ])}
        ]
    }
}
LOOKUP_JSON = {
    'absolute_magnitude_h': 18.11, 
    'close_approach_data':  [
        make_cad('2003-11-12', '18.6789574595', '6.012210062'),
        make_cad('2022-10-04', '27.7096935217', '5.9936492672'),
        make_cad('2042-02-28', '16.901207815', '8.6360960897')
    ],
	'designation': '65803', 
	'estimated_diameter': {
		'feet': {
			'estimated_diameter_max': 4656.1292775265, 
			'estimated_diameter_min': 2082.2843153153
		}, 
		'kilometers': {
			'estimated_diameter_max': 1.4191881584, 
			'estimated_diameter_min': 0.634680239
		}, 
		'meters': {
			'estimated_diameter_max': 1419.1881583761, 
			'estimated_diameter_min': 634.6802389983
		}, 
		'miles': {
			'estimated_diameter_max': 0.8818423652, 
			'estimated_diameter_min': 0.3943718948
		}
	}, 
	'id': '2065803', 
	'is_potentially_hazardous_asteroid': 'True', 
	'is_sentry_object': 'False', 
	'links': {
		'self': 'http://api.nasa.gov/neo/rest/v1/neo/2065803'
	}, 
	'name': '65803 Didymos (1996 GT)', 
	'name_limited': 'Didymos', 
	'nasa_jpl_url': 'https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html', 
	'neo_reference_id': '2065803', 
	'orbital_data': {
		'aphelion_distance': '2.272069974547477', 
		'ascending_node_longitude': '72.9858236207145', 
		'data_arc_in_days': '896', 
		'eccentricity': '.3831233242624545', 
		'epoch_osculation': '2461200.5', 
		'equinox': 'J2000', 
		'first_observation_date': '2022-09-27', 
		'inclination': '3.413876519313629', 
		'jupiter_tisserand_invariant': '4.204', 
		'last_observation_date': '2025-03-11', 
		'mean_anomaly': '260.8612886320632', 
		'mean_motion': '.4681261239466357', 
		'minimum_orbit_intersection': '.039575', 
		'observations_used': '1869', 
		'orbit_class': {
			'orbit_class_type': 'APO', 
			'orbit_class_description': 'Near-Earth asteroid', 
			'orbit_class_range': 'a > 1.0 AU; q < 1.017 AU'
		}, 
		'orbit_determination_date': '2026-03-01 16:49:59', 
		'orbit_id': '240', 
		'orbit_uncertainty': '0', 
		'orbital_period': '769.0235207660371', 
		'perihelion_argument': '319.5807001349104', 
		'perihelion_distance': '1.013349242511927', 
		'perihelion_time': '2461412.277780167719', 
		'semi_major_axis': '1.642709608529702'
	}
}


@pytest.fixture
def feed_df():
    """Returns a dataframe of FEED_JSON"""
    return neows.build_dataframe(FEED_JSON)


@pytest.fixture
def lookup_df():
    """Returns a dataframe of LOOKUP_JSON"""
    return neows.build_dataframe(LOOKUP_JSON)