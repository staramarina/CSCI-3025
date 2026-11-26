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
        Note: "Date" and "Amount" always exist per parsing rules
        
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
        date_full = pd.date_range(
            data["Date"].min(), 
            data["Date"].max(), 
            freq="D"
        )
        data = (data.set_index("Date")
                    .reindex(date_full, fill_value=0)
                    .rename_axis("Date")
                    .reset_index())
        data["Amount"] *= -1
        exp_min = data["Amount"].min().round(2) + 0.0
        exp_max = data["Amount"].max().round(2) + 0.0
        exp_avg = data["Amount"].mean().round(2) + 0.0
        return (data, exp_min, exp_max, exp_avg)

    def spend_chart(self):
        """Generates the chart for overall spending per day
        
        Args:
            None
        
        Returns:
            chart: a 2-tuple with the following format
                [0]: matplotlib figure
                [1]: matplotlib axes
        """
        data, exp_min, exp_max, exp_avg = self.spend_analysis()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(
            data=data,
            x="Date",
            y="Amount",
            color="tab:blue",
            dashes=False,
            estimator=None,
            label="Daily Expense Total",
            ax=ax,
        )
        ax.axhline(
            exp_max, ls="--", color="tab:red", 
            label=f"Maximum Daily Expense: {exp_max:.2f}"
        )
        ax.axhline(
            exp_avg, ls="--", color="tab:orange", 
            label=f"Average Daily Expense: {exp_avg:.2f}"
        )
        ax.axhline(
            exp_min, ls="--", color="tab:green", 
            label=f"Minimum Daily Expense: {exp_min:.2f}"
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
        """Performs analysis on spending by category
        Note: "Amount" is required per parser, "Category" is optional
        
        Args:
            None
        
        Returns:
            A 2-tuple with the following format:
                [0]: True if Category column exists, otherwise False
                [1]: data in a dataframe on success, otherwise error message
        """
        if "Category" in self.df.columns:
            data = self.df.loc[self.df["Amount"] < 0,
                               ["Category", "Amount"]].copy()
            data = data.dropna()
            data = data.groupby("Category", as_index=False)["Amount"].sum()
            data = data.sort_values(by="Amount", ascending=False)
            data = data.reset_index(drop=True)
            data["Amount"] *= -1
            return (True, data)
        else:
            return (False, "Category data not available")

    def cat_chart(self):
        """Generates the chart for spending by category
        
        Args:
            None
        
        Returns:
            A 2-tuple with the following format
                [0]: True if Category column exists, otherwise False
                [1]: a 2-tuple of matplotlib (fig, ax) on success, 
                     otherwise error message
        """
        check = self.cat_analysis()
        if check[0]:
            data = check[1]
            fig, ax = plt.subplots(figsize=(10, max(4, 0.4*len(data))))
            sns.barplot(
                data=data,
                x="Amount",
                y="Category",
                color="tab:blue",
                errorbar=None,
                ax=ax
            )
            ax.set_title("Total Expenses by Category")
            ax.set_xlabel("Total Amount")
            ax.set_ylabel("")
            for con in ax.containers:
                ax.bar_label(con, fmt="%.2f", padding=3)
            ax.margins(x=0.12)
            fig.tight_layout()
            chart = (fig, ax)
            return (True, chart)
        else:
            return (False, check[1])


    def descript_analysis(self):
        """Performs analysis on spending by description
        Note: "Amount" is required per parser, "Description" is optional
        
        Args:
            None
        
        Returns:
            A 2-tuple with the following format:
                [0]: True if Description column exists, otherwise False
                [1]: data in a dataframe on success, otherwise error message
        """
        # Do this off description if exists, else send error
        # probably don't need any extra calcs for this, just return df

    def descript_chart(self):
        """Generates the chart for spending by description
        
        Args:
            None
        
        Returns:
            A 2-tuple with the following format
                [0]: True if Description column exists, otherwise False
                [1]: a 2-tuple of matplotlib (fig, ax) on success, 
                     otherwise error message
        """
        # probably bar chart for this

    def bal_analysis(self):
        """Performs analysis on overall balance changes per day
        Note: "Amount" is required per parser, "Balance" is optional
        
        Args:
            None
        
        Returns:
            A 2-tuple with the following format:
                [0]: True if Balance column exists, otherwise False
                [1]: data in a dataframe on success, otherwise error message
        """
        # need date and balance, check for later, otherwise send error
        # probably don't need anything else, just return df

    def bal_chart(self):
        """Generates the chart for overall balances changes per day
        
        Args:
            None
        
        Returns:
            A 2-tuple with the following format
                [0]: True if Balance column exists, otherwise False
                [1]: a 2-tuple of matplotlib (fig, ax) on success, 
                     otherwise error message
        """
        # probably bar/whisker to show the distribution of changes, otherwise line plot

    def top5_analysis(self):
        """Performs analysis on top 5 expenses
        Note: "Amount" is required per parser, "Description" is optional
        
        Args:
            None
        
        Returns:
            A 2-tuple with the following format:
                [0]: True if Description column exists, otherwise False
                [1]: data in a dataframe on success, otherwise error message
        """
        # need description and amount, check for description, otherwise send error
        # consolidate on description
        # find the top 5 expenses
        # return 2 df, one for each top 5, then another for everything else to compare

    def top5_chart(self):
        """Generates the chart for top 5 expenses
        
        Args:
            None
        
        Returns:
            A 2-tuple with the following format
                [0]: True if Description column exists, otherwise False
                [1]: a 2-tuple of matplotlib (fig, ax) on success, 
                     otherwise error message
        """
        check = self.top5_analysis()
        if check[0]:
            data = check[1]
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.pie(
                data["Amount"],
                labels=data["Description"],
                autopct="%1.11f%%",
                startangle=90,
                counterclock=False
            )
            ax.set_title("Top 5 Expenses")
            ax.axis("equal")
            fig.tight_layout()
            chart = (fig, ax)
            return (True, chart)
        else:
            return (False, check[1])
