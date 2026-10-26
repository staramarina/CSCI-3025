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


class TestInLib:
    """Class to test book_in_exists(self, book), find_book(self, isbn), 
       patron_exists(self, patron), and find_patron(self, card) methods"""


    def test_book_present(self, sample_lib, sample_book_many):
        """Tests whether true is returned when book is present"""
        sample_lib.books[sample_book_many.isbn] = sample_book_many
        flag = sample_lib.book_in_exists(sample_book_many)
        assert flag


    def test_book_absent(self, sample_lib, sample_book_many):
        """Tests whether false is return when book is absent"""
        flag = sample_lib.book_in_exists(sample_book_many)
        assert not flag


    def test_book_key_presesnt(self, sample_lib, sample_book_many):
        """Tests whether the book is returned when given an existing key"""
        sample_lib.books[sample_book_many.isbn] = sample_book_many
        book = sample_lib.find_book('9780141439518')
        assert book.isbn == sample_book_many.isbn
        assert book.author == sample_book_many.author
        assert book.title == sample_book_many.title
        assert book.qty == sample_book_many.qty


    def test_book_key_absent(self, sample_lib, sample_book_many):
        """Tests whether None is returned when given an absent book key"""
        book = sample_lib.find_book('9780141439518')
        assert book is None


    def test_patron_present(self, sample_lib, sample_patron):
        """Tests whether true is returned when patron is present"""
        sample_lib.patrons[sample_patron.card_num] = sample_patron
        flag = sample_lib.patron_exists(sample_patron)
        assert flag


    def test_patron_absent(self, sample_lib, sample_patron):
        """Tests whether false is return when patron is absent"""
        flag = sample_lib.patron_exists(sample_patron)
        assert not flag


    def test_patron_key_presesnt(self, sample_lib, sample_patron):
        """Tests whether the patron is returned when given an existing key"""
        sample_lib.patrons[sample_patron.card_num] = sample_patron
        patron = sample_lib.find_patron('899261678')
        assert patron.card_num == sample_patron.card_num
        assert patron.last_name == sample_patron.last_name
        assert patron.first_name == sample_patron.first_name


    def test_patron_key_absent(self, sample_lib, sample_patron):
        """Tests whether None is returned when given an absent patron key"""
        patron = sample_lib.find_patron('899261678')
        assert patron is None


class TestAddBook:
    """Class to test the add_book(self, book) method"""


    def test_update_pass(self, samp_pop_lib, sample_book_single):
        """Tests the case when book already exists and adding passes"""
        flag = samp_pop_lib.add_book(sample_book_single)
        assert flag
        assert 2 == samp_pop_lib.books[sample_book_single.isbn].tot_qty
        assert 2 == samp_pop_lib.books[sample_book_single.isbn].qty


    def test_add_new(self, sample_lib, sample_book_single):
        """Tests the case when a book does not already exist"""
        flag = sample_lib.add_book(sample_book_single)
        assert flag