# Tiffany M. Mui
# Module 4 Assignment
# CSCI-3025: Python Programming
# Purpose: Demonstrate functions and handling errors
# Sources: NIST. (2024). SP 365: Metric Conversion Card. 
#     https://doi.org/10.6028/NIST.SP.365-2024


def menu_input_check(UserInput = "No Input"):
    """Checks the format of user input from the selection menu.
    
    Returns 0 for quit parameter.
    Returns 1 for valid selection format.
    Returns 2 for invalid selection format."""
    if 'q' == UserInput:
        CheckFlag = 0
    else:
        try:
            UserInput = int(UserInput)
            CheckFlag = 1
        except:
            CheckFlag = 2
    return CheckFlag


def number_check(UserInput = "No Input"):
    """Checks the format of the number entered to convert.
    
    Returns 1 for valid number format.
    Returns 2 for invalid number format."""
    try:
        UserInput = float(UserInput)
        CheckFlag = 1
    except:
        CheckFlag = 2
    return CheckFlag


def menu_select_check(UserInput = 0):
    """Checks if the selected menu option is available."""
    if 0 < UserInput < 9:
        CheckFlag = 1
    else: 
        CheckFlag = 2
    return CheckFlag


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
    print("1 -- inches (in)")
    print("2 -- miles (mi)")
    print("3 -- centimeters (cm)")
    print("4 -- kilometers (km)")
    print("5 -- pounds (lbs)")
    print("6 -- kilograms (kg)")
    print("7 -- Fahrenheit (F)")
    print("8 -- Celsius (C)")
    print("q -- Quit")
    MenuSelect = input()
    MenuCheck = menu_input_check(MenuSelect)
    if 0 == MenuCheck:
        print("\nThank you for using the unit conversion calculator!")
    elif 1 == MenuCheck:
        print(MenuCheck) #testing line remove later
        #TODO build program
    elif 2 == MenuCheck:
        print("\nAn invalid selection was made.")
        print("Please run the program again and select a menu number.")
    else: 
        print("\nAn unknown error ocurred.")