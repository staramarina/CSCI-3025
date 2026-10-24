# Tiffany M. Mui
# Module 6 Assignment - Patron Class Module
# CSCI-3025: Python Programming
# Purpose: Patron and Educator classes with associated attributes and methods
# Dependencies: TBD


class Parton:
    """Provides information on and support actions of patrons"""


    def __init__(self, num = '0', last = '', first = '', dob = None, 
                 phone = '', email = '', address = ''):
        """Initializes an instance of the Patron class
        
        Args:
            num: Unique library card number
            last: Patron's last name
            first: Patron's first name
            dob: Patron's date of birth
            phone: Patron's phone number
            email: Patron's email address
            address: Patron's residential address
        
        Returns:
            Patron instance
        """
        self.card_num = num
        self.last_name = last
        self.first_name = first
        self.dob = dob # TODO: write function to convert this to datetime
        self.phone = phone
        self.email = email
        self.address = address
        self.standing = 'good'
        self.books = {}