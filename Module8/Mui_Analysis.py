# Tiffany M. Mui
# Module 8 Assignment - Analysis Module
# CSCI-3025: Python Programming
# Purpose: Functions to handle specific analysis
# Dependencies: pandas, seaborn, matplotlib


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mplticker


# First analysis: PHO vs. non-PHO per day, with comparing averages
def neo_pho_trim(data):
    """Trims data for analysis and plotting of PHO vs. non-PHO per day 
    with comparing averages
    
    Args:
        data: feed pandas dataframe with values in expected formats 
              (from clean_common_data)
    
    Returns:
        trim: trimmed dataframe with only close_approach_date_full and 
              is_potentially_hazardous_asteroid values, with
              missing values removed
    """
    pho_map = {
        True: 'PHO',
        False: 'Not PHO'
    }
    trim = data[['close_approach_date_full',
            'is_potentially_hazardous_asteroid']].copy()
    trim.rename(columns={'close_approach_date_full': 'date', 
            'is_potentially_hazardous_asteroid': 'pho_status'}, inplace=True)
    trim = trim.dropna()
    trim = trim.sort_values(by='date')
    trim['date'] = pd.to_datetime(trim['date']).dt.date
    trim['pho_status'] = trim['pho_status'].map(pho_map)
    return trim


def neo_avg_calc(trim):
    """Calculates average PHO statistics
    
    Args:
        trim: trimmed pandas dataframe from neo_pho_trim
    
    Returns:
        neo_avg: a 3-tuple of the following format
            [0]: average number of non-PHO for given dates
            [1]: average number of PHO for given dates
            [2]: average number of total NEO for given dates
    """
    pho_val = ['PHO', 'Not PHO']
    df = trim.copy()
    count = (df.groupby(['date', 'pho_status']).size()
             .unstack(fill_value=0)
             .reindex(columns=pho_val, fill_value=0)
             .sort_index())
    not_pho_avg = count['Not PHO'].mean()
    pho_avg = count['PHO'].mean()
    tot_avg = count.sum(axis=1).mean()
    neo_avg = (not_pho_avg, pho_avg, tot_avg)
    return neo_avg
    

def neo_pho_chart(data):
    """Generates a clustered column chart of PHO/non-PHO per day 
    with average comparison lines
    
    Args:
        data: feed pandas dataframe with values in expected formats 
              (from clean_common_data)
    
    Returns:
        chart: a 2-tuple with the following format
            [0]: matplotlib figure
            [1]: matplotlib axes
    """
    trim = neo_pho_trim(data)
    avg = neo_avg_calc(trim)
    day = sorted(trim['date'].unique())
    palette = sns.color_palette()[:2]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=trim, x = 'date', hue = 'pho_status', 
            hue_order=['Not PHO', 'PHO'], order=day, palette=palette, ax=ax)
    ax.axhline(avg[0], ls='--', color=palette[0], 
            label=f'Mean non-PHO/day: {avg[0]:.2f}')
    ax.axhline(avg[1], ls=':', color=palette[1],
            label=f'Mean PHO/day: {avg[1]:.2f}')
    ax.set_title('Near-Earth Objects per Day (Close Approach)')
    ax.set_xlabel('Date (Close Approach)')
    ax.set_ylabel('Number of NEOs')
    ax.legend()
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    fig.tight_layout()
    chart = (fig, ax)
    return chart


# Second analysis: Lunar close approach per day with comparing average
def lun_miss_trim(data):
    """Trims data for analysis and plotting of lunar miss distance per day 
    with comparing averages
    
    Args:
        data: feed pandas dataframe with values in expected formats 
              (from clean_common_data)
    
    Returns:
        trim: trimmed dataframe with only close_approach_date_full and 
              miss_distance_lunar values, with missing values removed
    """
    trim = data[['close_approach_date_full',
            'miss_distance_lunar']].copy()
    trim.rename(columns={'close_approach_date_full': 'date', 
            'miss_distance_lunar': 'd_miss'}, inplace=True)
    trim = trim.dropna()
    trim = trim.sort_values(by='date')
    trim['date'] = pd.to_datetime(trim['date']).dt.date
    return trim


def lun_miss_chart(data):
    """Generates box-and-whisker chart of lunar miss distance per day
    
    Args:
        data: feed pandas dataframe with values in expected formats 
              (from clean_common_data)
    
    Returns:
        chart: a 2-tuple with the following format
            [0]: matplotlib figure
            [1]: matplotlib axes
    """
    trim = lun_miss_trim(data)
    day = sorted(trim['date'].unique())
    mean_all = trim['d_miss'].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=trim, x='date', y='d_miss', order=day, ax=ax)
    ax.axhline(mean_all, ls='--', color='red', 
            label=f'Overall mean: {mean_all:.2f} lunar')
    ax.set_title('Miss Distance (Lunar) per Day (Close Approach)')
    ax.set_xlabel('Date (Close Approach)')
    ax.set_ylabel('Miss Distance (Lunar)')
    ax.legend()
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    fig.tight_layout()
    chart = (fig, ax)
    return chart


# Third analysis: Compare min/max diameter of all PHOs, compare against Didymos
def pho_size_trim(data):
    """Trims data for analysis and plotting of min/max diameter of PHO 
    per day with comparison against Didymos
    
    Args:
        data: feed pandas dataframe with values in expected formats 
              (from clean_common_data)
    
    Returns:
        trim: long format trimmed dataframe with min/max and estimated 
              diameter columns of only PHOs with missing values removed
    """
    mask = data['is_potentially_hazardous_asteroid'].eq(True).fillna(False)
    trim = data.loc[mask, [ 'close_approach_date_full', 
            'meters_estimated_diameter_min', 
            'meters_estimated_diameter_max']].copy()
    trim.rename(columns={
        'close_approach_date_full': 'date',
        'meters_estimated_diameter_min': 'min_diameter',
        'meters_estimated_diameter_max': 'max_diameter'
    }, inplace=True)
    trim = trim.dropna()
    trim = trim.sort_values(by='date')
    trim['date'] = pd.to_datetime(trim['date']).dt.date
    trim = (trim.groupby('date')[['min_diameter', 'max_diameter']]
            .mean().rename(columns={
                'min_diameter': 'Estimated min diameter (m)',
                'max_diameter': 'Estimated max diameter (m)'
            }))
    trim = trim.reset_index().melt(id_vars = 'date',
            var_name = 'diameter', value_name = 'diameter_m')
    return trim


def pho_size_chart(data, didymos_data):
    """Generates bar chart of diameters of all PHOs per day,
    with comparison against Didymos

    Args:
        data: feed pandas dataframe with values in expected formats 
              (from clean_common_data)
        didymos_data: lookup pandas dataframe for Didymos
                      (from clean_lookup_data)
    
    Returns:
        chart: a 2-tuple with the following format
            [0]: matplotlib figure
            [1]: matplotlib axes
    """
    trim = pho_size_trim(data)
    dm_min = float(didymos_data['meters_estimated_diameter_min'].iloc[0])
    dm_max = float(didymos_data['meters_estimated_diameter_max'].iloc[0])
    palette = sns.color_palette()[:2]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=trim, x='date', y='diameter_m', hue = 'diameter',
            hue_order=['Estimated min diameter (m)', 
            'Estimated max diameter (m)'], palette=dict(zip(
                ['Estimated min diameter (m)', 'Estimated max diameter (m)'], 
                palette)), ax=ax)
    ax.axhline(dm_min, ls='--', color=palette[0], 
            label=f'Didymos min: {dm_min:.2f}')
    ax.axhline(dm_max, ls='--', color=palette[1], 
            label=f'Didymos max: {dm_max:.2f}')
    ax.set_title('PHO Estimated Diameters/Day vs. Didymos')
    ax.set_xlabel('Date (Close Approach)')
    ax.set_ylabel('Estimated diameter (m)')
    ax.legend()
    ax.set_yscale('log') # TODO may not need this, check display
    fig.tight_layout()
    chart = (fig, ax)
    return chart


# Fourth analysis: Didymos Mars vs Earth with miss distance
def didymos_orbit_trim(data):
    """Trims data for analysis and plotting of Didymos orbiting patterns
    
    Args: 
        data: lookup pandas dataframe for Didymos with values in expected 
              formats (from clean_lookup_data)
    
    Returns:
        trim: trimmed dataframe with only close_approach_date_full, 
              miss_distance_lunar, and orbiting_body values, with
              missing values removed
    """
    trim = data.loc[
        data['orbiting_body'].isin(['Earth', 'Mars']),
        ['close_approach_date_full', 'miss_distance_lunar', 'orbiting_body']
    ].copy()
    trim = trim.dropna()
    trim = trim.sort_values(by='close_approach_date_full')
    trim['year'] = pd.to_datetime(trim['close_approach_date_full']).dt.year
    return trim


def didymos_orbit_chart(data):
    """Generates a scatter plot of Didymos miss distance by flyby body
    
    Args:
        data: lookup pandas dataframe for Didymos in expected formats
              (from clean_lookup_data)
    
    Returns:
        chart: a 2-tuple with the following format
            [0]: matplotlib figure
            [1]: matplotlib axes
    """
    dart_impact = 2022 + (269/365)
    trim = didymos_orbit_trim(data)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(
        data=trim, x='year', 
        y='miss_distance_lunar', hue='orbiting_body',
        style='orbiting_body', markers=['s', 'o'],
        markersize=8, dashes=False, estimator=None, ax=ax
    )
    ax.axvline(dart_impact, ls='-.', color='grey',
            label='DART Impact (26 Sep 2022)')
    ax.xaxis.set_major_locator(mplticker.MaxNLocator(integer=True))
    ax.set_title('Didymos Miss Distance (Lunar) by Flyby Body')
    ax.set_xlabel('Year (Close Approach)')
    ax.set_ylabel('Miss Distance (Lunar)')
    ax.legend(title='Flyby Body')
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    fig.tight_layout()
    chart = (fig, ax)
    return chart