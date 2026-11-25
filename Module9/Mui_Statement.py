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
        self.name = name  # TODO validate this as well to strip any directories from the file name
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
