# Tiffany M. Mui
# Module 8 Assignment - Analysis Module
# CSCI-3025: Python Programming
# Purpose: Functions to handle specific analysis
# Dependencies: 
#   Standard: TBD
#   External: pandas, seaborn, matplotlib
#   Custom: TBD


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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
    trim['date'] = pd.to_date(trim['date']).dt.date
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
    sns.countplot(data=trim, x = 'date', hue = 'pho_status', hue_order=['PHO',
            'Not PHO'], order=day, palette=palette, ax=ax)
    ax.axhline(avg[1], ls='--', color=palette[0], 
            label=f'Mean non-PHO/day: {avg[1]:.2f}')
    ax.axline(avg[0], ls=':', color=palette[1],
            label=f'Mean PHO/day: {avg[0]:.2f}')
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
    trim['date'] = pd.to_date(trim['date']).dt.date
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
    ax.axhline(mean_all, ls='--', label=f'Overall mean: {mean_all}:.2f lunar')
    ax.set_title('Miss Distance (Lunary) per Day (Close Approach)')
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
    with comparison against Didymos
    
    Args:
        data: feed pandas dataframe with values in expected formats 
              (from clean_common_data)
    
    Returns:
        trim: long format trimmed dataframe with min/max and estimated 
              diameter columns of only PHOs with missing values removed
    """
    mask = data['is_potentially_hazardous_asteroid'].eq(True).fillna(False)
    pho = data.loc[mask, ['meters_estimated_diameter_min', 
            'meters_estimated_diameter_max']].dropna()
    trim = pho.melt(var_name='diameter', value_name='diameter_m')
    label_map = {
        'meters_estimated_diameter_min': 'Estimated min diameter (m)',
        'meters_estimated_diameter_max': 'Estimated max diameter (m)'
    }
    trim['diameter'] = trim['diameter'].replace(label_map)
    return trim


def pho_size_chart(data, didymos_data):
    """Generates box-and-whisker chart to distribution of diameters of all PHOs,
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
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=trim, x='diameter', y='diameter_m',
            order=['Estimated min diameter (m)', 'Estimated max diameter (m)'],
            ax=ax)
    ax.axhline(dm_min, ls='--', label=f'Didymos min: {dm_min}:.2f')
    ax.axhline(dm_max, ls='--', label=f'Didymos max: {dm_max}:.2f')
    ax.set_title('PHO Estimated Diameters vs. Didymos')
    ax.set_xlabel('')
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
        data: feed pandas dataframe with values in expected formats 
              (from clean_lookup_data)
    
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
    return trim


def didymos_orbit_chart(data):
    """Generated a scatter plot of Didymos miss distance by flyby body
    
    Args:
        data: lookup pandas dataframe for Didymos in expected formats
              (from clean_lookup_data)
    
    Returns:
        chart: a 2-tuple with the following format
            [0]: matplotlib figure
            [1]: matplotlib axes
    """
    trim = didymos_orbit_trim(data)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=trim, x='close_approach_date_full', 
        y='miss_distance_lunar', hue='orbiting_body',
        style='orbiting_body', s=60, ax=ax
    )
    ax.set_title('Didymos Miss Distance (Lunar) by Flyby Body')
    ax.set_xlabel('Date (Close Approach)')
    ax.set_ylabel('Miss Distance (Lunar)')
    ax.legend(title='Flyby Body')
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    fig.tight_layout()
    chart = (fig, ax)
    return chart