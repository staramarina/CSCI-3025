# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for Mui_Patron.py module
# Run with: pytest tests/test_patron.py -v


import sys
from pathlib import Path
from datetime import datetime, timedelta

#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tests.utilities import offset_date
from Mui_Patron import Educator


class TestPatronConstructor:
    """Class to test the __init__ method"""


    def test_default_values(self, sample_patron_default):
        """Tests that default values are populated when args are missing"""
        assert '111222333' == sample_patron_default.card_num
        assert '' == sample_patron_default.last_name
        assert '' == sample_patron_default.first_name
        assert None == sample_patron_default.dob
        assert '' == sample_patron_default.phone
        assert '' == sample_patron_default.email
        assert '' == sample_patron_default.address


    def test_init_values(self, sample_patron_default):
        """Tests initialization values that are the same for all patrons"""
        assert 'good' == sample_patron_default.standing
        assert 0 == len(sample_patron_default.books)


    def test_populated_values(self, sample_patron):
        """Tests that passed values override defaults"""
        assert '899261678' == sample_patron.card_num
        assert 'Deckow' == sample_patron.last_name
        assert 'Sonia' == sample_patron.first_name
        assert '19711012' == sample_patron.dob
        assert '810-932-7365' == sample_patron.phone
        assert 'soniadeckow@protonmail.com' == sample_patron.email
        assert '9740 Larissa Expressway Apt. 320, Bernitaport, South Dakota, 07123' == sample_patron.address


class TestPatronString:
    """Class to test the __str__ method"""


    def test_str_format(self, sample_patron):
        """Tests that string appears as expected"""
        expect = ('Card #: 899261678 - Deckow, Sonia')
        assert expect == str(sample_patron)


    def test_str_default(self, sample_patron_default):
        """Tests that a book with default values prints as expected"""
        expect = ('Card #: 111222333 - , ')
        assert expect == str(sample_patron_default)


class TestPatronCheckoutBook:
    """Class to test the checkout_book(self, book) method"""


    def test_success_checkout(self, sample_patron, sample_book_many):
        """Tests the successful checkout of a book"""
        flag = sample_patron.checkout_book(sample_book_many)
        assert flag[0]
        assert sample_book_many.isbn in sample_patron.books
        assert 14 == sample_book_many.qty
        assert 1 == sample_patron.books[sample_book_many.isbn].qty
        assert None != sample_patron.books[sample_book_many.isbn].return_date


    def test_duplicate_checkout(self, sample_patron, sample_book_many):
        """Tests the duplicate checkout branch"""
        flag0 = sample_patron.checkout_book(sample_book_many)
        flag1 = sample_patron.checkout_book(sample_book_many)
        assert flag0[0]
        assert not flag1[0]
        assert 'already checked out' in flag1[1]


    def test_checkout_limit(self, sample_patron, sample_book_many, 
                            sample_book_single):
        """Tests reaching the checkout limit"""
        sample_patron.books = {
            '1': 'Book One',
            '2': 'Book Two',
            '3': 'Book Three',
            '4': 'Book Four',
            '5': 'Book Five',
            '6': 'Book Six',
            '7': 'Book Seven',
            '8': 'Book Eight',
            '9': 'Book Nine',
            '10': 'Book Ten',
            '11': 'Book Eleven'
        }
        flag0 = sample_patron.checkout_book(sample_book_many)
        flag1 = sample_patron.checkout_book(sample_book_single)
        assert flag0[0]
        assert not flag1[0]
        assert 'Cannot exceed checkout limit' in flag1[1]


class TestReturnBook:
    """Class to test the return_book(self, book) method"""


    def test_success_return(self, sample_patron, sample_book_many):
        """Tests successfully returning a book"""
        sample_patron.checkout_book(sample_book_many)
        flag = sample_patron.return_book(sample_book_many)
        assert flag[0]
        assert 15 == sample_book_many.qty
        assert 'successfully returned' in flag[1]


    def test_fail_return(self, sample_patron, sample_book_single):
        """Tests failing to return a book"""
        flag = sample_patron.return_book(sample_book_single)
        assert not flag[0]
        assert 'not checked out' in flag[1]


class TestPatronCheckoutExtend:
    """Class to test the checkout_extend(self, book) method"""


    def test_hold_fail(self, sample_patron, sample_book_single):
        """Tests the failure branch due to a hold on the book"""
        sample_patron.checkout_book(sample_book_single)
        sample_book_single.hold_start = offset_date(days=-5)
        sample_book_single.hold_end = offset_date(days=5)
        flag = sample_patron.checkout_extend(sample_book_single)
        assert not flag[0]
        assert 'Book is on hold' in flag[1]


    def test_hold_pass(self, sample_patron, sample_book_many):
        """Tests the success branch, hold, but sufficient quantity"""
        sample_patron.checkout_book(sample_book_many)
        sample_patron.books[sample_book_many.isbn].return_date = (
                offset_date(weeks=-2))
        orig_return = sample_patron.books[sample_book_many.isbn].return_date
        sample_book_many.hold_start = offset_date(days=-5)
        sample_book_many.hold_end = offset_date(days=5)
        sample_book_many.hold_qty = 5
        flag = sample_patron.checkout_extend(sample_book_many)
        new_return = sample_patron.books[sample_book_many.isbn].return_date
        assert flag[0]
        assert orig_return < new_return
        assert 'successfully extended' in flag[1]


    def test_wait_fail(self, sample_patron, sample_book_single):
        """Tests that extending the checkout fails when there is a waitlist"""
        sample_patron.checkout_book(sample_book_single)
        sample_book_single.waitlist.append('111222333')
        flag = sample_patron.checkout_extend(sample_book_single)
        assert not flag[0]
        assert 'Book is waitlisted' in flag[1]


    def test_not_checked(self, sample_patron, sample_book_single):
        """Tests that attempting to return a book not checked out fails"""
        flag = sample_patron.checkout_extend(sample_book_single)
        assert not flag[0]
        assert 'not currently checked out' in flag[1]


class TestWaitlistAdd:
    """Class to test the waitlist_add(self, book) method"""


    def test_checked_out(self, sample_patron, sample_book_single):
        """Tests that adding to waitlist for checked out book fails"""
        sample_patron.checkout_book(sample_book_single)
        flag = sample_patron.waitlist_add(sample_book_single)
        assert not flag[0]
        assert 'already have that book' in flag[1]


    def test_add_wait(self, sample_patron, sample_book_single):
        """Tests that a patron is successfully added to the waitlist"""
        flag = sample_patron.waitlist_add(sample_book_single)
        assert flag[0]
        assert 0 == flag[1]


    def test_wait_already(self, sample_patron, sample_book_single):
        """Tests that a patron's position in the waitlist is not changed"""
        sample_patron.waitlist_add(sample_book_single)
        sample_book_single.waitlist.append('112233')
        sample_book_single.waitlist.append('445566')
        flag = sample_patron.waitlist_add(sample_book_single)
        assert flag[0]
        assert 0 == flag[1]


class TestEducatorConstructor:
    """Class to test the Educator __init__ method"""


    def test_default_values(self, sample_ed_default):
        """Tests that default values behave as expected with inheritance"""
        assert '444555666' == sample_ed_default.card_num
        assert '' == sample_ed_default.last_name
        assert '' == sample_ed_default.first_name
        assert None == sample_ed_default.dob
        assert '' == sample_ed_default.phone
        assert '' == sample_ed_default.email
        assert '' == sample_ed_default.address
        assert '' == sample_ed_default.institution
        assert isinstance(sample_ed_default, Educator)


    def test_real_values(self, sample_educator):
        """Tests that real values overwrite defaults with inheritance"""
        assert '888120722' == sample_educator.card_num
        assert 'Barrows' == sample_educator.last_name
        assert 'Americo' == sample_educator.first_name
        assert '19881015' == sample_educator.dob
        assert '580-438-9671' == sample_educator.phone
        assert 'americo.barrows68@outlook.com' == sample_educator.email
        assert '5677 Witting Rest Suite 120, East Harmony, California, 66444' == sample_educator.address
        assert 'P.S. 112' == sample_educator.institution
        assert isinstance(sample_educator, Educator)


class TestCurrentHold:
    """Class to test the hold_book(self, book) method"""


    def test_no_holds(self, sample_educator, sample_book_single):
        """Tests when there is nothing in the hold books list"""
        flag = sample_educator.hold_book(sample_book_single)
        assert not flag[0]
        assert 'no books on hold' in flag [1]


    def test_too_early(self, sample_educator, sample_book_single):
        """Tests when the hold has not started yet"""
        sample_book_single.hold_start = offset_date(days=3)
        sample_book_single.hold_end = offset_date(days=15)
        sample_educator.hold_books[sample_book_single.isbn] = (
                sample_book_single)
        flag = sample_educator.hold_book(sample_book_single)
        assert not flag[0]
        assert 'window has not started' in flag [1]


    def test_too_late(self, sample_educator, sample_book_single):
        """Tests when the hold has expired"""
        sample_book_single.hold_start = offset_date(days=-15)
        sample_book_single.hold_end = offset_date(days=-3)
        sample_educator.hold_books[sample_book_single.isbn] = (
                sample_book_single)
        flag = sample_educator.hold_book(sample_book_single)
        assert not flag[0]
        assert 'window has ended' in flag [1]


    def test_not_hold(self, sample_educator, sample_book_single):
        """Tests when there is a hold book list, but the book isn't on it"""
        sample_educator.hold_books['123456789'] = 'On-Hold Book'
        flag = sample_educator.hold_book(sample_book_single)
        assert not flag[0]
        assert 'do not have a hold on the book' in flag [1]

    def test_hold_active(self, sample_educator, sample_book_single):
        """Tests when a hold is active"""
        sample_book_single.hold_start = offset_date(days=-2)
        sample_book_single.hold_end = offset_date(days=17)
        sample_book_single.hold_qty = 1
        sample_educator.hold_books[sample_book_single.isbn] = (
                sample_book_single)
        flag = sample_educator.hold_book(sample_book_single)
        assert flag[0]
        assert 1 == flag [1]


class TestEdCheckoutBook:
    """Class to test the Educator checkout_book(self, book) method"""

    def test_hold_checkout(self, sample_educator, sample_book_single):
        """Tests when a book is on hold and checkout is successful"""
        sample_book_single.hold_start = offset_date(days=-2)
        sample_book_single.hold_end = offset_date(days=17)
        sample_book_single.hold_qty = 1
        sample_educator.hold_books[sample_book_single.isbn] = (
                sample_book_single)
        flag = sample_educator.checkout_book(sample_book_single)
        assert flag[0]
        assert 'successfully checked out' in flag[1]

    def test_not_enough(self, sample_educator, sample_book_many):
        """Tests when a book is on hold, but there aren't enough"""
        sample_book_many.hold_start = offset_date(days=-2)
        sample_book_many.hold_end = offset_date(days=17)
        sample_book_many.hold_qty = 5
        sample_book_many.qty = 3
        sample_educator.hold_books[sample_book_many.isbn] = (
                sample_book_many)
        flag = sample_educator.checkout_book(sample_book_many)
        assert flag[0]
        assert 'successfully checked out' in flag[1]

    def test_reg_checkout(self, sample_educator, sample_book_many):
        """Tests when there is a hold, but book_hold check fails"""
        sample_book_many.hold_start = offset_date(days=3)
        sample_book_many.hold_end = offset_date(days=15)
        sample_book_many.hold_qty = 1
        sample_educator.hold_books[sample_book_many.isbn] = (
                sample_book_many)
        flag = sample_educator.checkout_book(sample_book_many)
        assert flag[0]
        assert 'successfully checked out' in flag[1]


class TestHoldRequest:
    """Class to test the hold_request(self, book, start, end, qty) method"""

    def test_old_hold(self, sample_educator, sample_book_single):
        """Tests when the book is already on hold"""
        start = offset_date(days=10)
        end = offset_date(days=30)
        qty = 1
        sample_educator.hold_books[sample_book_single.isbn] = (
                sample_book_single)
        flag = sample_educator.hold_request(sample_book_single, start, end, qty)
        assert not flag[0]
        assert 'already on hold' in flag[1]


    def test_many_hold(self, sample_educator, sample_book_single):
        """Tests when there aren't enough books for a hold"""
        start = offset_date(days=10)
        end = offset_date(days=30)
        qty = 5
        flag = sample_educator.hold_request(sample_book_single, start, end, qty)
        assert not flag[0]
        assert 'more than available quantity' in flag[1]
    

    def test_past_hold(self, sample_educator, sample_book_single):
        """Tests when a hold is requested for past dates"""
        start = offset_date(days=-7)
        end = offset_date(days=-3)
        qty = 1
        flag = sample_educator.hold_request(sample_book_single, start, end, qty)
        assert not flag[0]
        assert 'hold for past dates' in flag[1]

    def test_end_start(self, sample_educator, sample_book_single):
        """Tests when the start date is after the end date"""
        start = offset_date(days=10)
        end = offset_date(days=5)
        qty = 1
        flag = sample_educator.hold_request(sample_book_single, start, end, qty)
        assert not flag[0]
        assert 'end date before start date' in flag[1]

        
    def test_hold_success(self, sample_educator, sample_book_single):
        """Tests when a hold is placed successfully"""
        start = offset_date(days=10)
        end = offset_date(days=30)
        qty = 1
        flag = sample_educator.hold_request(sample_book_single, start, end, qty)
        assert flag[0]
        assert 'added to hold list' in flag[1]


class TestHoldUpdate:
    """Class to test the hold_update(self, book, start, end) method"""
class TestHoldCancel:
    """Class to test the hold_remove(self, book) method"""