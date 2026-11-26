# Tiffany M. Mui
# Module 9 Assignment - Statement Class Module
# CSCI-3025: Python Programming
# Purpose: Class for bank statements, analysis, and chart generation
# Dependencies: pandas


import pandas as pd


class Statement:
    """Holds and provides methods for transaction data"""

    def __init__(self, data, name="Transaction Data"):
        """Initiatlizes a statement class instance
        
        Args:
            name: name of the data set (typically the file name)
            data: a pandas dataframe
        
        Returns:
            A statement class instance
        """
        self.name = name
        self.df = data

    @property
    def df(self):
        """Used for validated access to statement's dataframe"""
        return self.__df

    def _val_df(self, data):
        """Checks that input data is a pandas dataframe
        
        Args:
            data: a pandas dataframe
        
        Raises:
            TypeError: if data is not a pandas dataframe
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError('Data must be in a pandas dataframe')
        else:
            return data

    @df.setter
    def df(self, data):
        """Sets the dataframe after validation
        
        Args:
            data: a pandas dataframe
        
        Returns:
        """
        self.__df = self._val_df(data)

    def __str__(self):
        """Provides file name and data for a statement as a string"""
        title = str(self.name)
        data = self.df.to_string(header=True, index=True)
        return(f'{title}\n{data}')

    def __add__(self, other):
        """Adds two statement instances together and returns a new combined 
        statement instance"""
        new_name = f'{self.name}, {other.name}'
        new_dfa = self.df.copy()
        new_dfb = other.df.copy()
        if "File Source" not in self.df.columns:
            new_dfa["File Source"] = [str(self.name)] * len(self.df)
        if "File Source" not in other.df.columns:
            new_dfb["File Source"] = [str(other.name)] * len(other.df)
        new_df = pd.concat([new_dfa, new_dfb], ignore_index=True)
        new_df = new_df.sort_values(by="Date")
        new_df = new_df.reset_index(drop=True)
        return Statement(new_df, new_name)

    def spend_analysis(self):
        """Performs analysis on overall spending per day"""
        # just need date and amount columns (both required per cleaning)
        # remove all NA (date already done in cleaning)
        # remove any positive, then * -1 to all
        # calculate min, max, mean
        # return df, min, max, mean

    def spend_chart(self):
        """Generates the chart for overall spending per day"""
        # do lineplot
        # do hlines for min, max, and mean expense per day

    def cat_analysis(self):
        """Performs analysis on spending by category"""
        # Check that category exists, otherwise send error
        # just need category and amount
        # calculate percentage of spend on each category, put it in a dict
        # return df and percentage dict

    def cat_chart(self):
        """Generates the chart for spending by category"""
        # do a pie chart with matplotlib for this, seaborn doesn't support

    def descript_analysis(self):
        """Performs analysis on spending by description"""
        # Do this off description if exists, else send error
        # probably don't need any extra calcs for this, just return df

    def descript_chart(self):
        """Generates the chart for spending by description"""
        # probably bar chart for this

    def bal_analysis(self):
        """Performs analysis on overall balance changes per day"""
        # need date and balance, check for later, otherwise send error
        # probably don't need anything else, just return df

    def bal_chart(self):
        """Generates the chart for overall balances changes per day"""
        # probably bar/whisker to show the distribution of changes, otherwise line plot

    def top5_analysis(self):
        """Performs analysis on top 5 expenses"""
        # need description and amount, check for description, otherwise send error
        # consolidate on description
        # find the top 5 expenses
        # return 2 df, one for each top 5, then another for everything else to compare

    def top5_chart(self):
        """Generates the chart for top 5 expenses"""
        # probably just a bar chart, maybe compare against all other categories combined
