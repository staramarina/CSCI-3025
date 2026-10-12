# Tiffany M. Mui
# Module 5 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for Mui_M5Calculations.py module
# Run with: pytest tests/test_calculations.py -v


import sys
from pathlib import Path
from decimal import Decimal


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


import Mui_M5Calculations as calc


class TestGenerateBudgetObject:
    """Tests the generate_budget_object() function"""


    def test_generate_structure(self, valid_budget_data):
        """Calls and checks generate_budget_object()
        
        Args:
            valid_budget_data: name of the file that contains the data
        
        Returns:
            None
        """
        budget = calc.generate_budget_object(str(valid_budget_data))

        assert isinstance(budget, dict)
        assert 3 == len(budget)
        assert ['Salary', 'bimonthly', '2764.81'] == budget[0]
        assert ['Bonus', 'yearly', '1500.00'] == budget[1]
        assert ['Other', 'monthly', '941.26'] == budget[2]


    def test_empty_file(self, tmp_path):
        """Tests that empty file will return an empty dictionary
        
        Args:
            tmp_path: file path to the created file
        
        Returns:
            None
        """
        file_path = tmp_path / "empty.txt"
        file_path.write_text("")
        budget = calc.generate_budget_object(str(file_path))

        assert {} == budget


class TestCheckBudgetData:
    """Tests the check_budget_data() function"""


    def test_valid_data_return(self, sample_income_dict):
        """Tests that valid data will return empty removed lines dictionary
        
        Args:
            sample_income_dict: a dictionary with elements as a list containing 
                the following expected budgetary data
                [0]: unique name of the item as a string
                [1]: frequency of the transaction as a string
                [2]: dollar amount of the transaction as a decimal
        
        Returns:
            None
        """
        listed = calc.check_budget_data(sample_income_dict)

        assert {} == listed


    def test_wrong_length(self):
        """Tests that lines of wrong length are flagged and listed"""
        bad_data = {
            0 : ['Valid Line', 'monthly', '100.00'],
            1 : ['Wrong Length', '50.00']
        }
        listed = calc.check_budget_data(bad_data)

        assert 1 in listed
        assert ("Reason: list does not contain the expected number of elements" 
                in listed[1][-1])


    def test_invalid_frequency(self):
        """Tests that invalid frequencies are flagged and listed"""
        bad_data = {
            0 : ['Valid Line', 'monthly', '100.00'],
            1 : ['Invalid Frequency', 'monthy', '789.45']
        }
        listed = calc.check_budget_data(bad_data)

        assert 1 in listed
        assert ("Reason: frequency is not an accepted value" 
                in listed[1][-1])


    def test_invalid_amount(self):
        """Tests that dollar amounts are flagged and listed"""
        bad_data = {
            0 : ['Valid Line', 'monthly', '100.00'],
            1 : ['Invalid Dollar Amount', 'yearly', 'one-hundred']
        }
        listed = calc.check_budget_data(bad_data)

        assert 1 in listed
        assert ("Reason: dollar amount is not a decimal" 
                in listed[1][-1])


    def test_none_amount(self):
        """Tests that dollar amount of none is flagged and listed"""
        bad_data = {
            0 : ['Valid Line', 'monthly', '100.00'],
            1 : ['Invalid Dollar Amount', 'yearly', None]
        }
        listed = calc.check_budget_data(bad_data)
        
        assert 1 in listed
        assert ("Reason: dollar amount is not a decimal" 
                in listed[1][-1])


    def test_duplicate_name(self):
        """Tests that invalid frequencies are flagged and listed"""
        bad_data = {
            0 : ['Valid Line', 'monthly', '100.00'],
            1 : ['Duplicate Name', 'quarterly', '12.45'],
            2 : ['Duplicate Name', 'semiannually', '45.78']
        }
        listed = calc.check_budget_data(bad_data)

        assert 1 in listed
        assert 2 in listed
        assert ("Reason: line item does not have a unique name" 
                in listed[1][-1])
        assert ("Reason: line item does not have a unique name" 
                in listed[2][-1])


class TestFormatBudgetData:
    """Tests the format_budget_data function"""


    def test_frequency_case(self):
        """Tests that frequency matching is not case sensitive"""
        data = {
            0: ['Item0', 'Monthly', '1000.00'],
            1: ['Item1', 'monthly', '200.00']
        }
        formatted = calc.format_budget_data(data)

        assert 12 == formatted['Item0'][0]
        assert 12 == formatted['Item1'][0]

    
    def test_calc_multiplier(self, sample_income_dict):
        """Tests that frequencies are converted to numerical multipliers
        
        Args:
            sample_income_dict: a dictionary with elements as a list containing 
                    the following expected budgetary data
                [0]: unique name of the item as a string
                [1]: frequency of the transaction as a string
                [2]: dollar amount of the transaction as a decimal
        
        Returns:
            None
        """
        formatted = calc.format_budget_data(sample_income_dict)

        assert 24 == formatted['Income 1'][0]
        assert 12 == formatted['Income 2'][0]


    def test_convert_decimal(self, sample_income_dict):
        """Tests that the dollar amounts convert to decimals
        
        Args:
            sample_income_dict: a dictionary with elements as a list containing 
                    the following expected budgetary data
                [0]: unique name of the item as a string
                [1]: frequency of the transaction as a string
                [2]: dollar amount of the transaction as a decimal
                
        Returns:
            None
        """
        formatted = calc.format_budget_data(sample_income_dict)

        assert isinstance(formatted['Income 1'][1], Decimal)
        assert Decimal('3671.18') == formatted['Income 1'][1]


class TestYearlyConversion:
    """Tests the yearly_conversion function"""


    def test_keys(self, sample_format_income):
        """Tests that keys remain unchanged after calculations
        
        Args:
            sample_format_income: a dictionary with list elements containing 
                    budgetary data in the following format
                key: name of the item as a string
                [0]: frequency of the transaction per year as an integer
                [1]: dollar amount of the transaction as a decimal
        
        Returns:
            None
        """
        yearly = calc.yearly_conversion(sample_format_income)

        assert 'Income 1' in yearly
        assert 'Income 2' in yearly


    def test_yearly_conversion(self, sample_format_income):
        """Tests that dollar amounts are calculated to yearly values
        
        Args:
            sample_format_income: a dictionary with list elements containing 
                    budgetary data in the following format
                key: name of the item as a string
                [0]: frequency of the transaction per year as an integer
                [1]: dollar amount of the transaction as a decimal

        Returns:
            None
        """
        yearly = calc.yearly_conversion(sample_format_income)

        assert Decimal('88108.32') == yearly['Income 1'][0]
        assert Decimal('21701.40') == yearly['Income 2'][0]


class TestSumIncome:
    """Tests the sum_income function"""


    def test_sum_all_income(self, sample_yearly_income):
        """Tests that all income sources are added
        
        Args:
            sample_yearly_income: a dictionary with list elements containing 
                    budgetary data in the following format
                key: name of the item as a string
                [0]: yearly dollar amount of the transaction as a decimal
        
        Returns:
            None
        """
        total = calc.sum_income(sample_yearly_income)

        assert Decimal('109809.72') == total


    def test_empty_income(self):
        """Tests that empty income returns Decimal(0)"""
        total = calc.sum_income({})

        assert Decimal('0') == total


class TestBudgetCalc:
    """Tests the budget_calc function"""


    def test_monthly_div(self, sample_yearly_income):
        """Tests that yearly amounts are divided by 12 as expected
        
        Args:
            sample_yearly_income: a dictionary with list elements containing 
                    budgetary data in the following format
                key: name of the item as a string
                [0]: yearly dollar amount of the transaction as a decimal
                
        Returns:
            None
        """
        monthly = calc.budget_calc(sample_yearly_income, Decimal('109809.72'))

        assert Decimal('7342.36') == monthly['Income 1'][0]
        assert Decimal('1808.45') == monthly['Income 2'][0]


    def test_percent_cal(self, sample_yearly_income):
        """Tests that percentages are performed as (item / yearly_total) x 100
        
        Args:
            sample_yearly_income: a dictionary with list elements containing 
                    budgetary data in the following format
                key: name of the item as a string
                [0]: yearly dollar amount of the transaction as a decimal
                
        Returns:
            None
        """
        monthly = calc.budget_calc(sample_yearly_income, Decimal('109809.72'))
        percent = float(monthly['Income 1'][1])

        assert 80.0 < percent < 80.5


    def test_percent_sum(self, sample_yearly_income):
        """Tests that the sum of all percentages is approximately 100%
        
        Args:
            sample_yearly_income: a dictionary with list elements containing 
                    budgetary data in the following format
                key: name of the item as a string
                [0]: yearly dollar amount of the transaction as a decimal
                
        Returns:
            None
        """
        monthly = calc.budget_calc(sample_yearly_income, Decimal('109809.72'))
        percent_tot = sum(item[1] for item in monthly.values())

        assert 99.9 < percent_tot < 100.1


class TestBudgetRounding:
    """Tests the budget_rounding function"""


    def test_round_two(self):
        """Tests that values are rounded as strings with two decimal places"""
        data = {
            'Item0' : [Decimal('12.3456'), Decimal('45.789')],
            'Item1' : [Decimal('99.999'), Decimal('0.4444')]
        }
        rounded = calc.budget_rounding(data)

        assert ['12.35', '45.79'] == rounded['Item0']
        assert ['100.00', '0.44'] == rounded['Item1']


    def test_string_output(self):
        """Tests that the output is of string type, not Decimal"""
        data = {
            'Item' : [Decimal('123'), Decimal('45')]
        }
        rounded = calc.budget_rounding(data)

        assert isinstance(rounded['Item'][0], str)
        assert isinstance(rounded['Item'][1], str)


class TestEdgeCases:
    """Tests additional edge cases"""


    def test_large_num(self):
        """Tests that large numbers can maintain precision"""
        large = {
            'High Income' : [1, Decimal('999999.99')]
        }
        total = calc.sum_income(large)

        assert Decimal('999999.99') == total


    def test_small_round(self):
        """Tests that small numbers are rounded properly"""
        small = {
            'Small Number' : [Decimal('0.005'), Decimal('0.004')]
        }
        rounded = calc.budget_rounding(small)

        assert ['0.01', '0.00'] == rounded['Small Number']