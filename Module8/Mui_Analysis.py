# Tiffany M. Mui
# Module 8 Assignment - Analysis Module
# CSCI-3025: Python Programming
# Purpose: Functions to handle specific analysis
# Dependencies: 
#   Standard: TBD
#   External: TBD
#   Custom: TBD

# First analysis: PHO vs. non-PHO per day over two weeks, with comparing averages
# TODO: function for trimming to just PHO data, should only need close_approach_date_full on X and is_potentially_hazardous_asteroid on Y, make sure clean and ordered
# TODO: function to bucket True/False PHO data by day, calculate average of each, then calculate total NEO qty avg
# TODO: function to generate clustered column chart with average lines
# TODO: function to display chart (put in ancillary as general chart use)

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