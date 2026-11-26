# Tiffany M. Mui
# Module 9 Assignment - Statement Class Module
# CSCI-3025: Python Programming
# Purpose: Class for bank statements, analysis, and chart generation
# Dependencies: pandas


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mplticker


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
        """Performs analysis on overall spending per day
        
        Args:
            None
        
        Returns:
            data: expense data only grouped by date
            exp_min: minimum daily expense total
            exp_max: maximum daily expense total
            exp_avg: average daily expense total
        """
        data = self.df.loc[self.df["Amount"] < 0,["Date", "Amount"]].copy()
        data = data.dropna()
        data = data.groupby("Date", as_index=False)["Amount"].sum()
        data = data.sort_values(by="Date")
        data = data.reset_index(drop=True)
        data["Amount"] *= -1
        exp_min = data["Amount"].min().round(2)
        exp_max = data["Amount"].max().round(2)
        exp_avg = data["Amount"].mean().round(2)
        return (data, exp_min, exp_max, exp_avg)

    def spend_chart(self):
        """Generates the chart for overall spending per day
        
        Args:
            None
        
        Returns:
        """
        data, exp_min, exp_max, exp_avg = self.spend_analysis()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(
            data=data,
            x="Date",
            y="Amount",
            markersize=8,
            dashes=False,
            estimator=None,
            ax=ax,
        )
        ax.axhline(
            exp_min, ls="--", label=f"Minimum Daily Expense: {exp_min:.2f}"
        )
        ax.axhline(
            exp_max, ls="--", label=f"Maximum Daily Expense: {exp_max:.2f}"
        )
        ax.axhline(
            exp_avg, ls="--", label=f"Average Daily Expense: {exp_avg:.2f}"
        )
        ax.set_title("Aggregate Expenses per Day")
        ax.set_xlabel("Date")
        ax.set_ylabel("Aggregate Amount")
        ax.legend(title="Statistics")
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
        fig.tight_layout()
        chart = (fig, ax)
        return chart

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
