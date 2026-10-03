# Tiffany M. Mui
# Module 4 Assignment
# CSCI-3025: Python Programming
# Purpose: Demonstrate functions and handling errors
# Sources: NIST. (2024). SP 365: Metric Conversion Card. 
#     https://doi.org/10.6028/NIST.SP.365-2024


def input_menu():
    """Prints user input options and returns user input.
    User input validated by separate function."""
    print("1 -- inches (in)")
    print("2 -- miles (mi)")
    print("3 -- centimeters (cm)")
    print("4 -- kilometers (km)")
    print("5 -- pounds (lbs)")
    print("6 -- kilograms (kg)")
    print("7 -- Fahrenheit (F)")
    print("8 -- Celsius (C)")
    print("q -- Quit")
    UserInput = input()
    return UserInput


def menu_select_check(UserInput):
    if 'q' == UserInput:
        CheckFlag = 0
    else: 
        # TODO write try statement to check for int input
    return CheckFlag

def number_check(UserInput):
    # TODO write check to validate numerical values


def in_to_cm(inch):
    """Convert inches to centimeters."""
    cm = inch * 2.54
    return cm

def cm_to_in(cm):
    """Convert centimeters to inches."""
    inch = cm / 2.54
    return inch

def mi_to_km(mile):
    """Convert miles to kilometers."""
    km = mile * 1.61
    return km

def km_to_mi(km):
    """Convert kilometers to miles."""
    mile = km / 1.61
    return mile

def lb_to_kg(pound):
    """Convert pounds to kilograms."""
    kg = pound * 0.45
    return kg

def kg_to_lb(kg):
    """Convert kilograms to pounds."""
    pound = kg / 0.45
    return pound

def fah_to_cel(fah):
    """Convert degrees Fahrenheit to degrees Celsius"""
    cel = (fah - 32) / 1.8
    return cel

def cel_to_fah(cel):
    """Convert degrees Celsius to degrees Fahrenheit"""
    fah = (cel * 1.8) + 32
    return fah


if __name__ == "__main__":
    """Main function that runs the unit conversion program."""
    print("Select the number corresponding to the input unit (or q to quit)")
    InputUnit = input_menu()
    print(InputUnit)