# Tiffany M. Mui
# Module 8 Assignment - Analysis Module
# CSCI-3025: Python Programming
# Purpose: Functions to handle specific analysis
# Dependencies: 
#   Standard: TBD
#   External: TBD
#   Custom: TBD


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# First analysis: PHO vs. non-PHO per day over two weeks, with comparing averages
# TODO: function for trimming to just PHO data, should only need close_approach_date_full on X and is_potentially_hazardous_asteroid on Y, make sure clean and ordered
def neo_pho_trim(data):
    """Trims data for analysis and plotting of PHO vs. non-PHO per day 
    with comparing averages
    
    Args:
        data: feed pandas dataframe with values in expected formats 
              (from clean_common_data)
    
    Returns:
        trim: trimmed dataframe with only close_approach_date_full and 
                   is_potentially_hazardous_asteroid columns, with
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

# TODO: function to bucket True/False PHO data by day, calculate average of each, then calculate total NEO qty avg
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
    
# TODO: function to generate clustered column chart with average lines
def neo_pho_chart(data):
    """Generates a clustered column chart of PHO/non-PHO per day 
    with average comparison lines
    
    Args:
        data: feed pandas dataframe with values in expected formats 
              (from clean_common_data)
    
    Returns:
        graph: a 2-tuple with the following format
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
    graph = (fig, ax)
    return graph




# Second analysis: Lunar close approach per day with comparing average
# TODO: function for trimming to just lunar close data, should only need close_approach_date_full on X, miss_distance_lunar on Y, make sure clean and ordered
# TODO: function to find values for bar/whisker chart (may not need, check chart options)
# TODO: function to generate bar/whisker chart with average lines

# Third analysis: Compare min/max diameter of all PHOs, compare against Didymos
# TODO: function for trimming to just PHO true data, then trim columns to close_approach_date_full (X), meters_estimated_diameter_max and meters_estimated_diameter_min (Y)
# TODO: function to find values for bar/whisker chart (may not need, check chart options)
# TODO: function to generate bar/whisker chart with Didymos comparison lines

# Fourth analysis: Didymos Mars vs Earth with miss distance
# TODO: function to trim/separate close approach data, one for Earth one for Mars, then trim columns to close_approach_date_full (X) and miss_distance_lunar (Y)
# TODO: function to generate scatter plot chart