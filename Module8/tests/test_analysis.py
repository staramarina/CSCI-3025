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
        1006, '2026-11-03 19:10', False,
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


@pytest.fixture
def feed_data():
    """Returns a pandas dataframe mimicking clean feed data"""
    return pd.DataFrame(FEED_DATA)


@pytest.fixture
def orbit_data():
    """Returns a pandas dataframe mimicking clean Didymos data"""
    return pd.DataFrame(ORBIT_DATA)


@pytest.fixture
def didymos_diameter():
    """returns a single-row pandas dataframe for Didymos diameter data"""
    diameter = pd.DataFrame([{
        'meters_estimated_diameter_min': DIDYMOS_MIN,
        'meters_estimated_diameter_max': DIDYMOS_MAX
    }])
    return diameter


@pytest.fixture(autouse=True)
def close_plot():
    """Closes charts after each test"""
    yield
    plt.close('all')


def hline_label(ax):
    """Collects labels of reference lines
    
    Args:
        ax: matplotlib axes
    
    Returns:
        label: list of labels from objects on the axes
    """
    label = []
    for line in ax.lines:
        label.append(line.get_label())
    return label


class TestNeoPhoTrim:
    """Class to test the neo_pho_trim function"""


    def test_neo_rename(self, feed_data):
        """Tests that columns are renamed to date and pho_status"""
        data = analysis.neo_pho_trim(feed_data)
        assert 'date' in data.columns
        assert 'pho_status' in data.columns
        assert 'close_approach_date_full' not in data.columns


    def test_orig_change(self, feed_data):
        """Tests that the original dataframe is unchanged"""
        analysis.neo_pho_trim(feed_data)
        assert 'close_approach_date_full' in feed_data.columns
        assert 'pho_status' not in feed_data.columns


    def test_neo_drop(self, feed_data):
        """Tests that rows with missing values are dropped"""
        data = analysis.neo_pho_trim(feed_data)
        assert 8 == len(data)
        assert not data.isna().any().any()


    def test_pho_map(self, feed_data):
        """Tests that PHO boolean is mapped to labels"""
        data = analysis.neo_pho_trim(feed_data)
        status = set(data['pho_status'].unique())
        assert {'PHO', 'Not PHO'} == status


    def test_neo_sort(self, feed_data):
        """Tests that dates are date objects and sorted"""
        data = analysis.neo_pho_trim(feed_data)
        dates = list(data['date'])
        assert isinstance(data['date'].iloc[0], date)
        assert dates == sorted(dates)


class TestNeoAvgCalc:
    """Class to test the neo_avg_calc function"""


    def test_avg_value(self, feed_data):
        """Tests that average is calculated correctly
        Expected counts per day:
            01 Nov - Non-PHO: 2, PHO: 2, Total: 4
            02 Nov - Non-PHO: 1, PHO: 2, Total 3
            03 Nov - Non-PHO: 1, PHO: 0, Total 1
        """
        exp_not_pho_avg = (2 + 1 + 1) / 3
        exp_pho_avg = (2 + 2 + 0) / 3
        exp_tot_avg = (4 + 3 + 1) / 3
        data = analysis.neo_pho_trim(feed_data)
        avg = analysis.neo_avg_calc(data)
        assert exp_not_pho_avg == avg[0]
        assert exp_pho_avg == avg[1]
        assert exp_tot_avg == avg[2]


    def test_zero_day(self):
        """Tests that days with no PHOs still count toward average"""
        data = pd.DataFrame({
            'date': [date(2026, 11, 1), date(2026, 11, 1), date(2026, 11, 2)],
            'pho_status': ['Not PHO', 'Not PHO', 'Not PHO']
        })
        exp_not_pho_avg = (2 + 1) / 2
        exp_pho_avg = 0
        exp_tot_avg = (2 + 1) / 2
        avg = analysis.neo_avg_calc(data)
        assert exp_not_pho_avg == avg[0]
        assert exp_pho_avg == avg[1]
        assert exp_tot_avg == avg[2]


class TestNeoPhoChart:
    """Class to test the neo_pho_chart function"""


    def test_neo_return_fig(self, feed_data):
        """Tests that both figure and axes is returned"""
        fig, ax = analysis.neo_pho_chart(feed_data)
        assert fig is not None
        assert ax is not None


    def test_neo_label(self, feed_data):
        """Tests that chart title and axis label are correct"""
        fig, ax = analysis.neo_pho_chart(feed_data)
        assert 'Near-Earth Objects per Day' in ax.get_title()
        assert 'Date' in ax.get_xlabel()
        assert 'Number of NEOs' in ax.get_ylabel()


    def test_neo_avg_label(self, feed_data):
        """Tests that both average lines are labeled"""
        exp_not_pho_avg = (2 + 1 + 1) / 3
        exp_pho_avg = (2 + 2 + 0) / 3
        fig, ax = analysis.neo_pho_chart(feed_data)
        label = hline_label(ax)
        non_pho = []
        pho = []
        for lab in label:
            if lab.startswith('Mean non-PHO/day'):
                non_pho.append(lab)
            elif lab.startswith('Mean PHO/day'):
                pho.append(lab)
        assert 1 == len(non_pho)
        assert 1 == len(pho)
        assert f'{exp_not_pho_avg:.2f}' in non_pho[0]
        assert f'{exp_pho_avg:.2f}' in pho[0]


class TestLunMissTrim:
    """Class to test the lun_miss_trim function"""


    def test_lun_rename(self, feed_data):
        """Tests that columns are renamed to date and d_miss"""
        data = analysis.lun_miss_trim(feed_data)
        assert 'date' in data.columns
        assert 'd_miss' in data.columns
        assert 'close_approach_date_full' not in data.columns


    def test_lun_drop(self, feed_data):
        """Tests that rows with missing values are dropped"""
        data = analysis.lun_miss_trim(feed_data)
        assert 8 == len(data)
        assert not data.isna().any().any()


    def test_lun_sort(self, feed_data):
        """Tests that dates are date objects and sorted"""
        data = analysis.lun_miss_trim(feed_data)
        dates = list(data['date'])
        assert isinstance(data['date'].iloc[0], date)
        assert dates == sorted(dates)


class TestLunMissChart:
    """Class to test the lun_miss_chart function"""


    def test_lun_return_fig(self, feed_data):
        """Tests that both figure and axes is returned"""
        fig, ax = analysis.lun_miss_chart(feed_data)
        assert fig is not None
        assert ax is not None


    def test_lun_label(self, feed_data):
        """Tests that chart title and axis label are correct"""
        fig, ax = analysis.lun_miss_chart(feed_data)
        assert 'Miss Distance (Lunar) per Day' in ax.get_title()
        assert 'Date' in ax.get_xlabel()
        assert 'Miss Distance (Lunar)' in ax.get_ylabel()


    def test_lun_avg_label(self, feed_data):
        """Tests that both average lines are labeled"""
        exp_avg = (119.264636 + 24.183183 + 118.764718 + 24.183388 + 67.962402 
                   + 179.038968 + 15.649873 + 140.499671) / 8
        fig, ax = analysis.lun_miss_chart(feed_data)
        label = hline_label(ax)
        lab_avg = []
        for lab in label:
            if lab.startswith('Overall mean'):
                lab_avg.append(lab)
        assert 1 == len(lab_avg)
        assert f'{exp_avg:.2f}' in lab_avg[0]


#class TestPhoSizeTrim:
    """Class to test the pho_size_trim function"""
#class TestPhoSizeChart:
    """Class to test the pho_size_chart function"""
#class TestDidymosOrbitTrim:
    """Class to test the didymos_orbit_trim function"""
#class TestDidymosOrbitChart:
    """Class to test the didymos_orbit_chart function"""







#lunar_distance = (119.264636 + 24.183183 + 118.764718 + 24.183388 + 67.962402 + 179.038968 + 15.649873 + 140.499671)
#min_dia = (513.517179 + 192.555078 + 30.517923 + 188.171989 + 205.378500 + 69.912523 + 63.760979)
#max_dia = (1148.259319 + 430.566244 + 68.240151 + 420.765360 + 459.240286 + 156.329154 + 142.573883)


