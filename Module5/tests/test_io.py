# Tiffany M. Mui
# Module 5 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for MuiIO.py module
# Run with: pytest tests/test_io.py -v


import sys
from pathlib import Path


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


import MuiIO as io


class TestFileExists:
    """Tests the file_exists function"""


    def test_file_exists_true(self, tmp_path):
        """Tests that (True, message) is returned when file exists
        
        Args:
            tmp_path: unique temporary directory file path

        Returns:
            None
        """
        test_file = tmp_path / "exists.txt"
        flag, message = io.file_exists(str(test_file))

        assert flag is True
        assert "exists" in message


    def test_file_not_exists(self):
        """Tests that (False, message) is returned when file does not exist"""
        flag, message = io.file_exists("not_file.txt")

        assert flag is False
        assert "does not exist" in message


    def test_directory(self, tmp_path):
        """Tests that path to directory returns (False, message)
        Args:
            tmp_path: unique temporary directory file path

        Returns:
            None
        """
        flag, message = io.file_exists(str(tmp_path))

        assert flag is False
        assert "not a file" in message


class TestCanWriteFile:
    """Tests the can_write_file function"""


    def test_writable_dir(self, tmp_path):
        """Tests that writing to writable directing succeeds
        Args:
            tmp_path: unique temporary directory file path

        Returns:
            None
        """
        test_file = tmp_path / "write_test.txt"
        flag, message = io.can_write_file(str(test_file))

        assert flag is True
        assert "exists" in message


    def test_restricted_dir(self):
        """Tests that writing to a restricted directory fails"""
        flag, message = io.can_write_file("/root_test.txt")
        print(f"Permission Result: {flag}, {message}")
        if flag:
            print("You probably shouldn't be running this as a super user.")
            print("File was saved in root if you want to delete it.")


class TestPrintNewFile:
    """Tests the print_new_file function"""


    def test_create_write(self, tmp_path):
        """Tests that file is created and contents are written
        Args:
            tmp_path: unique temporary directory file path

        Returns:
            None
        """
        test_file = tmp_path / "output.txt"
        data = {
            'Item0' : ['text', 123.45],
            'Item1' : ['more text', 67.89]
        }
        flag, message = io.print_new_file(str(test_file))

        assert flag is True
        assert "successfully" in message

        content = Path(test_file).read_text()
        assert "Item0" in content
        assert "text" in content
        assert "123.45" in content
        assert "Item1" in content
        assert "more text" in content
        assert "67.89" in content


    def test_append_file(self, tmp_path):
        """Tests that writing to a file appends new data, not overwritten
        Args:
            tmp_path: unique temporary directory file path

        Returns:
            None
        """
        test_file = tmp_path / "append_test.txt"
        io.print_new_file({0 : 'First Write'}, test_file)
        io.print_new_file({1 : 'Second Write'}, test_file)
        content = Path(test_file).read_text()
        lines = content.strip().split('\n')

        assert 2 == len(lines)
        assert 0 in lines[0]
        assert 1 in lines[1]


class TestIntegration:
    """Tests combining multiple functions"""


    def test_read_write(self, tmp_path):
        """Tests that reading and writing files can be done in sequence
        Args:
            tmp_path: unique temporary directory file path

        Returns:
            None
        """
        input_file = tmp_path / "input.txt"
        input_file.write_text("Test, monthly, 456.78")
        exists_flag, _ = io.file_exists(str(input_file))
        output_file = tmp_path / "output.txt"
        data = {'Another Test' : [123.00, 45.60]}
        write_flag, _ = io.file_exists(str(output_file))

        assert exists_flag is True
        assert write_flag is True
        assert output_file.exists()