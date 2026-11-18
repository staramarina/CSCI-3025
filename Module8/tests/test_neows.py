# Tiffany M. Mui
# Module 8 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for NeoWs Handle module
# Run with: pytest tests/test_neows.py -v


import sys
from pathlib import Path
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
            make_neo('1001', 'Test A', [
                make_cad('2026-11-01', '119.2646356882', '16.0941424487')
            ]),
            make_neo('1002', 'Test B', [
                make_cad('2026-11-01', '118.7647184455', '4.6212629351')
            ])
        ],
        '2026-11-02': [
            make_neo('1003', 'Test C', [
                make_cad('2026-11-02', '24.1831825905', '12.6714610504')
            ])
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
SAMPLE_URL = 'http://api.nasa.gov/neo/rest/v1/neo/'


@pytest.fixture
def feed_df():
    """Returns a dataframe of FEED_JSON"""
    return neows.build_dataframe(FEED_JSON)


@pytest.fixture
def lookup_df():
    """Returns a dataframe of LOOKUP_JSON"""
    return neows.build_dataframe(LOOKUP_JSON)


def make_feed_response(data = None, json_err = None, http_err = None):
    """Returns a mock response object for requests
    
    Args:
        data: Mock data that would be received from the API
        json_err: JSON error to raise instead of returning
        http_err: HTTP error to raise instead of returning
    
    Returns:
        r: A MagicMock object that responds like a request
    """
    r = MagicMock()
    r.raise_for_status.return_value = None
    if json_err is not None:
        r.json.side_effect = json_err
    elif http_err is not None:
        r.raise_for_status.side_effect = http_err
    else:
        if data is None:
            r.json.return_value = FEED_JSON
        else:
            r.json.return_value = data
    return r


def make_lookup_response(data = None, json_err = None, http_err = None):
    """Returns a mock response object for requests
    
    Args:
        data: Mock data that would be received from the API
        json_err: JSON error to raise instead of returning
        http_err: HTTP error to raise instead of returning
    
    Returns:
        r: A MagicMock object that responds like a request
    """
    r = MagicMock()
    r.raise_for_status.return_value = None
    if json_err is not None:
        r.json.side_effect = json_err
    elif http_err is not None:
        r.raise_for_status.side_effect = http_err
    else:
        if data is None:
            r.json.return_value = LOOKUP_JSON
        else:
            r.json.return_value = data
    return r


class TestEnvURL:
    """Class to test pulling the API key and building the query URLs"""


    def test_pull_key(self):
        """Tests pulling the API key from the env file
        Note: this is purposefully testing the local environment"""
        key = neows.load_env()
        assert key is not None


    def test_feed_url_good(self):
        """Tests the successful path of build_feed_url"""
        key = 'KEY'
        start = '2026-11-01'
        end = '2026-11-03'
        url = neows.build_feed_url(key, start, end)
        assert 'nasa.gov' in url
        assert 'feed' in url
        assert key in url
        assert start in url
        assert end in url


    def test_feed_bad_date(self, tmp_path):
        """Tests the bad end date path of build_feed_url"""
        key = 'KEY'
        start = '2026-11-01'
        end = '2026-Nov-03'
        log_file = tmp_path / "log.txt"
        url = neows.build_feed_url(key, start, end, err_log=str(log_file))
        assert '2026-10-29' in url
        assert log_file.exists()


    def test_lookup_url(self):
        """Tests that build_lookup_url is successful"""
        key = 'KEY'
        neo_id = '1234567'
        url = neows.build_lookup_url(key, neo_id)
        assert key in url
        assert neo_id in url


class TestNeoWsSuccess:
    """Class to test the successful path in neows_call function"""


    @patch("Mui_NeoWsHandle.requests.get")
    def test_feed_return(self, mock_get):
        """Tests that a mock call to feed endpoint returns mock feed data"""
        mock_get.return_value = make_feed_response()
        data = neows.neows_call(SAMPLE_URL)
        assert FEED_JSON == data


    @patch("Mui_NeoWsHandle.requests.get")
    def test_lookup_return(self, mock_get):
        """Tests that a mock call to feed endpoint returns mock feed data"""
        mock_get.return_value = make_lookup_response()
        data = neows.neows_call(SAMPLE_URL)
        assert LOOKUP_JSON == data


    @patch("Mui_NeoWsHandle.requests.get")
    def test_timeout_default(self, mock_get):
        """Tests that the timeout is the default if not specified"""
        mock_get.return_value = make_feed_response()
        neows.neows_call(SAMPLE_URL)
        mock_get.assert_called_once_with(SAMPLE_URL, timeout=10)


    @patch("Mui_NeoWsHandle.requests.get")
    def test_timeout_specified(self, mock_get):
        """Tests that the specified timeout is used when given"""
        mock_get.return_value = make_feed_response()
        neows.neows_call(SAMPLE_URL, timeout=5)
        mock_get.assert_called_once_with(SAMPLE_URL, timeout=5)


class TestNeoWsTimeout:
    """Class to test the timeout path in neows_call function"""


    @patch("Mui_NeoWsHandle.requests.get")
    def test_timeout_return(self, mock_get, tmp_path):
        """Tests that a timeout causes exit with code 1"""
        mock_get.side_effect = requests.exceptions.Timeout
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit) as exc_info:
            neows.neows_call(SAMPLE_URL, err_log=str(log_file))
        assert 1 == exc_info.value.code


    @patch("Mui_Logging.print_log")
    @patch("Mui_NeoWsHandle.requests.get")
    def test_timeout_print(self, mock_get, mock_print_log, capsys, tmp_path):
        """Tests that a timeout is logged and printed error points to logs"""
        mock_get.side_effect = requests.exceptions.Timeout(
                "Connection timed out")
        mock_print_log.return_value = (True, "File printed successfully")
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit):
            neows.neows_call(SAMPLE_URL, err_log=str(log_file))
        mock_print_log.assert_called_once()
        args, _ = mock_print_log.call_args
        assert isinstance(args[0], requests.exceptions.Timeout)
        assert str(log_file) == args[1]
        captured = capsys.readouterr()
        assert "An error occurred with the API" in captured.out
        assert "See" in captured.out
        assert str(log_file) in captured.out


class TestNeoWsHTTP:
    """Class to test the HTTP error path in neows_call function"""


    @patch("Mui_NeoWsHandle.requests.get")
    def test_http_none(self, mock_get, tmp_path):
        """Tests that an HTTP error causes exit with code 1"""
        err = requests.exceptions.HTTPError("401 Client Error: Unauthorized "
                "for url: http://api.nasa.gov/neo/rest/v1/neo/")
        mock_get.return_value = make_feed_response(http_err=err)
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit) as exc_info:
            neows.neows_call(SAMPLE_URL, err_log=str(log_file))
        assert 1 == exc_info.value.code


    @patch("Mui_Logging.print_log")
    @patch("Mui_NeoWsHandle.requests.get")
    def test_http_error(self, mock_get, mock_print_log, capsys, tmp_path):
        """Tests that HTTP error is logged and printed error points to logs"""
        err = requests.exceptions.HTTPError("401 Client Error")
        mock_get.return_value = make_feed_response(http_err=err)
        mock_print_log.return_value = (True, "File printed successfully")
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit):
            neows.neows_call(SAMPLE_URL, err_log=str(log_file))
        mock_print_log.assert_called_once()
        args, _ = mock_print_log.call_args
        assert isinstance(args[0], requests.exceptions.HTTPError)
        assert str(log_file) == args[1]
        captured = capsys.readouterr()
        assert "An error occurred with the API" in captured.out
        assert "See" in captured.out
        assert str(log_file) in captured.out


class TestNeoWsRequest:
    """Class to test the request exception path in neows_call function"""


    @patch("Mui_NeoWsHandle.err_handle")
    @patch("Mui_NeoWsHandle.requests.get")
    def test_connect_none(self, mock_get, mock_log, tmp_path):
        """Tests that a connection failure causes exit with code 1"""
        mock_get.side_effect = requests.exceptions.ConnectionError(
                "Connection refused")
        mock_log.return_value = (True, "File printed successfully")
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit) as exc_info:
            neows.neows_call(SAMPLE_URL, err_log=str(log_file))
        assert 1 == exc_info.value.code


    @patch("Mui_Logging.print_log")
    @patch("Mui_NeoWsHandle.requests.get")
    def test_req_err(self, mock_get, mock_print_log, capsys, tmp_path):
        """Tests that request error is logged and reported"""
        mock_get.side_effect = requests.exceptions.ConnectionError(
                "Connection refused")
        mock_print_log.return_value = (True, "File printed successfully")
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit):
            neows.neows_call(SAMPLE_URL, err_log=str(log_file))
        mock_print_log.assert_called_once()
        captured = capsys.readouterr()
        assert "An error occurred with the API" in captured.out
        assert "See" in captured.out
        assert str(log_file) in captured.out


class TestNeoWsJSON:
    """Class to test the value error path in neows_call function"""


    @patch("Mui_NeoWsHandle.requests.get")
    def test_json_none(self, mock_get, tmp_path):
        """Tests that bad JSON data causes exit with code 1"""
        err = ValueError("Expecting value: line 1 column 1")
        mock_get.return_value = make_feed_response(json_err=err)
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit) as exc_info:
            neows.neows_call(SAMPLE_URL, err_log=str(log_file))
        assert 1 == exc_info.value.code


    @patch("Mui_Logging.print_log")
    @patch("Mui_NeoWsHandle.requests.get")
    def test_json_err(self, mock_get, mock_print_log, capsys, tmp_path):
        """Tests that bad JSON data error is logged and reported"""
        err = ValueError("Expecting value: line 1 column 1")
        mock_get.return_value = make_feed_response(json_err=err)
        mock_print_log.return_value = (True, "File printed successfully")
        log_file = tmp_path / "log.txt"
        with pytest.raises(SystemExit):
            neows.neows_call(SAMPLE_URL, err_log=str(log_file))
        mock_print_log.assert_called_once()
        captured = capsys.readouterr()
        assert "An error occurred with the API" in captured.out
        assert "See" in captured.out
        assert str(log_file) in captured.out


class TestBuildDataframe:
    """Class to test the build_dataframe function"""


    def test_cad_exploded(self, feed_df):
        """Test that the cad data exploded results in correct row count"""
        assert 3 == len(feed_df)


    def test_dict_remain(self, feed_df):
        """Tests that no unflattened dictionaries are present"""
        dict_col = feed_df.columns[
            feed_df.apply(lambda col: col.map(type).eq(dict).any())
        ]
        assert 0 == len(dict_col)


    def test_nested_columns(self, feed_df):
        """Tests that all nested columns are flattened"""
        for col in [
            'close_approach_date_full',
            'miss_distance_lunar',
            'relative_velocity_kilometers_per_second',
            'meters_estimated_diameter_max'
        ]:
            assert col in feed_df.columns


    def test_lookup_build(self, lookup_df):
        """Tests that lookup specific rows are included when present"""
        for col in [
            'name_limited',
            'eccentricity',
            'orbit_class_orbit_class_type'
        ]:
            assert col in lookup_df.columns
        assert 3 == len(lookup_df)


    def test_empty_cad(self):
        """Tests the case when there is no close approach data (edge case)"""
        neo = {
            'near_earth_objects': {
                '2026-11-01': [
                    make_neo('3001', 'Test I', [])
                ]
            }
        }
        neo_df = neows.build_dataframe(neo)
        assert 1 == len(neo_df)


class TestTrimData:
    """Class to test data trimming functions"""


    def test_common_remove(self, feed_df):
        """Tests that intended common columns are removed"""
        trim = neows.trim_common_data(feed_df)
        for col in [
            'is_sentry_object',
            'neo_reference_id',
            'close_approach_date',
            'miss_distance_miles',
            'relative_velocity_miles_per_hour',
            'miles_estimated_diameter_min',
            'self'
        ]:
            assert col not in trim.columns


    def test_common_keep(self, feed_df):
        """Tests that intended common columns are kept"""
        trim = neows.trim_common_data(feed_df)
        for col in [
            'id',
            'is_potentially_hazardous_asteroid',
            'close_approach_date_full',
            'miss_distance_lunar',
            'relative_velocity_kilometers_per_second',
            'meters_estimated_diameter_max'
        ]:
            assert col in trim.columns


    def test_missing_column(self, feed_df):
        """Tests that missing column error is masked"""
        self_link_miss = feed_df.drop(columns=['self'])
        trim = neows.trim_common_data(self_link_miss)
        assert 'id' in trim.columns


    def test_lookup_remove(self, lookup_df):
        """Tests that intended specific lookup columns are removed"""
        trim = neows.trim_common_data(lookup_df)
        trim = neows.trim_lookup_data(trim)
        for col in [
            'designation',
            'name_limited',
            'equinox',
            'jupiter_tisserand_invariant',
            'orbit_class_orbit_class_description',
        ]:
            assert col not in trim.columns


    def test_lookup_keep(self, lookup_df):
        """Tests that intended specific lookup columns are kept"""
        trim = neows.trim_common_data(lookup_df)
        trim = neows.trim_lookup_data(trim)
        for col in [
            'eccentricity',
            'orbital_period',
            'semi_major_axis'
        ]:
            assert col in trim.columns


class TestCleanData:
    """Class to test data cleaning functions"""


    def test_num_convert(self, feed_df):
        """Tests that numbers in common columns are successfully converted"""
        trim = neows.trim_common_data(feed_df)
        clean = neows.clean_common_data(trim)
        for col in [
            'miss_distance_kilometers',
            'relative_velocity_kilometers_per_second',
            'meters_estimated_diameter_min'
        ]:
            assert pd.api.types.is_numeric_dtype(clean[col])


    def test_dtg_convert(self, feed_df):
        """Tests that date time groups in common columns are converted"""
        trim = neows.trim_common_data(feed_df)
        clean = neows.clean_common_data(trim)
        assert pd.api.types.is_datetime64_any_dtype(
            clean['close_approach_date_full']
        )


    def test_bool_map(self, feed_df):
        """Tests that PHO bool is successfully mapped and converted"""
        trim = neows.trim_common_data(feed_df)
        clean = neows.clean_common_data(trim)
        assert pd.api.types.is_bool_dtype(
            clean['is_potentially_hazardous_asteroid']
        )


    def test_duplicates(self):
        """Tests that duplicate rows are removed"""
        data = {
            'near_earth_objects': {
                '2026-11-01': [
                    make_neo('4001', 'Dup Test', [
                        make_cad('2026-11-01', '118.7647184455', '4.6212629351')
                    ]),
                    make_neo('4001', 'Dup Test', [
                        make_cad('2026-11-01', '118.7647184455', '4.6212629351')
                    ])
                ]
            }
        }
        df = neows.build_dataframe(data)
        trim = neows.trim_common_data(df)
        clean = neows.clean_common_data(trim)
        assert 1 == len(clean)


    def test_orbit_num(self, lookup_df):
        """Tests that lookup orbital data is converted to numbers"""
        trim = neows.trim_common_data(lookup_df)
        trim = neows.trim_lookup_data(trim)
        clean = neows.clean_common_data(trim)
        clean = neows.clean_lookup_data(clean)
        for col in [
            'ascending_node_longitude',
            'perihelion_argument',
            'perihelion_time'
        ]:
            assert pd.api.types.is_numeric_dtype(clean[col])


    def test_unique_cad(self, lookup_df):
        """Tests that unique cad for same ID is kept"""
        trim = neows.trim_common_data(lookup_df)
        trim = neows.trim_lookup_data(trim)
        clean = neows.clean_common_data(trim)
        clean = neows.clean_lookup_data(clean)
        assert 3 == len(clean)