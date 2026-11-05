# Tiffany M. Mui
# Module 7 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for Mui_Logging.py module
# Run with: pytest tests/test_logging.py -v

import sys
from pathlib import Path
from datetime import datetime


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


from Mui_Logging import print_log


class TestPrintLog:
    """Tests the print_log(data, file_name) function"""


    def test_print_new(self, tmp_path):
        """Tests that a new file can be generated and written to
        
        Args:
            tmp_path: unique temporary directory file path
        
        Returns:
            None
        """
        test_file = tmp_path / "log.txt"
        time_now = datetime.now()
        data = f'{time_now}: This is an error test.'
        flag = print_log(data, str(test_file))
        content = Path(test_file).read_text()
        assert flag[0]
        assert "successfully" in flag[1]
        assert str(time_now) in content
        assert "This is an error test" in content


    def test_append(self, tmp_path):
        """Tests that an existing file can be opened and appended
        
        Args:
            tmp_path: unique temporary directory file path
        
        Returns:
            None
        """
        time0 = datetime.now()
        data0 = f'{time0}: This is an error test.'
        time1 = datetime.now()
        data1 = f'{time1}: This is the append test.'
        test_file = tmp_path / "log_append.txt"
        flag0 = print_log(data0, str(test_file))
        flag1 = print_log(data1, str(test_file))
        content = Path(test_file).read_text()
        assert flag0[0]
        assert "successfully" in flag0[1]
        assert flag1[0]
        assert "successfully" in flag1[1]
        assert data0 in content
        assert data1 in content
