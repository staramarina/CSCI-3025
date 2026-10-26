# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for Mui_Library.py module
# Run with: pytest tests/test_library.py -v


class TestLibraryConstructor:
    """Tests the library __init__ method"""


    def test_default_lib(self, default_lib_default):
        """Tests that default values are populated when args are missing"""
        assert 'Library' == default_lib_default.name
        assert default_lib_default.phone is None
        assert default_lib_default.address is None


    def test_init_lib(self, default_lib_default):
        """Tests initialization values that are the same"""
        assert 0 == len(default_lib_default.books)
        assert 0 == len(default_lib_default.books_out)
        assert 0 == len(default_lib_default.patrons)


    def test_populated_lib(self, sample_lib):
        """Tests that passed values override defaults"""
        assert 'Mui Mini Library' == sample_lib.name
        assert '719-542-7279' == sample_lib.phone
        assert '123 S Academy Blvd, Fountain, CO 80819' == sample_lib.address