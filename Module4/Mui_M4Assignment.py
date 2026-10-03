# Tiffany M. Mui
# Module 4 Assignment
# CSCI-3025: Python Programming
# Purpose: Demonstrate functions and handling errors
# Sources: NIST. (2024). SP 365: Metric Conversion Card. 
#     https://doi.org/10.6028/NIST.SP.365-2024


IN_CM = 2.54 # Inches to centimeter conversion ratio
MI_KM = 1.609344 # Miles to kilometers conversion ratio
LB_KG = 0.45359237 # Pounds to kilograms conversion ratio


def menu_input_check(user_input = "No Input"):
    """Checks the format of user input from the selection menu.

    user_input is assumed to be a string with default value "No Input".
    Returns 0 for quit parameter.
    Returns 1 for valid selection format.
    Returns 2 for invalid selection format."""
    if 'q' == user_input:
        CheckFlag = 0
    else:
        try:
            user_input = int(user_input)
            CheckFlag = 1
        except:
            CheckFlag = 2
    return CheckFlag


def number_check(user_input = "No Input"):
    """Checks the format of the number entered to convert.
    
    user_input is assumed to be a string with default value "No Input".
    Returns 1 for valid number format.
    Returns 2 for invalid number format."""
    try:
        user_input = float(user_input)
        CheckFlag = 1
    except:
        CheckFlag = 2
    return CheckFlag


def menu_select_check(user_input = 0):
    """Checks if the selected menu option is available.
    
    user_input is assumed to be an integer with default value 0.
    Returns 1 if menu option is available.
    Returns 2 if selection is not available in the menu."""
    if 0 < user_input < 9:
        CheckFlag = 1
    else: 
        CheckFlag = 2
    return CheckFlag


def in_to_cm(inch):
    """Convert inches to centimeters.
    
    inch variable is assumed to be a number.
    Returns cm as a number.
    """
    cm = inch * IN_CM
    return cm


def cm_to_in(cm):
    """Convert centimeters to inches.
    
    cm variable is assumed to be a number.
    Returns inch as a number."""
    inch = cm / IN_CM
    return inch


def mi_to_km(mile):
    """Convert miles to kilometers.
    
    mile variable is assumed to be a number.
    Returns km as a number."""
    km = mile * MI_KM
    return km


def km_to_mi(km):
    """Convert kilometers to miles.
    
    km variable is assumed to a number.
    Returns mile as a number."""
    mile = km / MI_KM
    return mile


def lb_to_kg(pound):
    """Convert pounds to kilograms.
    
    pound variable is assumed to be a number.
    Returns kg as a number."""
    kg = pound * LB_KG
    return kg


def kg_to_lb(kg):
    """Convert kilograms to pounds.
    
    kg variable is assumed to be a number.
    Returns pound as a number."""
    pound = kg / LB_KG
    return pound


def fah_to_cel(fah):
    """Convert degrees Fahrenheit to degrees Celsius.
    
    fah variable assumed to be a number.
    Returns cel as a number."""
    cel = (fah - 32) / 1.8
    return cel


def cel_to_fah(cel):
    """Convert degrees Celsius to degrees Fahrenheit.
    
    cel variable assumed to be a number.
    Returns fah as a number."""
    fah = (cel * 1.8) + 32
    return fah


CONVERSION = {
    1: (in_to_cm, "in", "cm", "inches", "centimeters"),
    2: (mi_to_km, "mi", "km", "miles", "kilometers"),
    3: (cm_to_in, "cm", "in", "centimeters", "inches"),
    4: (km_to_mi, "km", "mi", "kilometers", "miles"),
    5: (lb_to_kg, "lb", "kg", "pounds", "kilograms"),
    6: (kg_to_lb, "kg", "lb", "kilograms", "pounds"),
    7: (fah_to_cel, "\N{DEGREE SIGN}F", "\N{DEGREE SIGN}C", 
        "Fahrenheit", "Celsius"),
    8: (cel_to_fah, "\N{DEGREE SIGN}C", "\N{DEGREE SIGN}F", 
        "Celsius", "Fahrenheit"),
}


def print_menu():
    """prints the menu options based on the conversion dictionary"""
    print("Select the number corresponding to the input unit (or q to quit)")
    for option, (_, short_unit, _, long_unit, _) in sorted(CONVERSION.items()):
        print(f"{option} -- {long_unit} ({short_unit})")
    print("q -- Quit")


if __name__ == "__main__":
    print_menu()
    menu_select = input()
    menu_check = menu_input_check(menu_select)
    if 0 == menu_check:
        print("\nThank you for using the unit conversion calculator!")
    elif 1 == menu_check:
        menu_select = int(menu_select)
        if menu_select in CONVERSION:
            convert_func, in_unit, out_unit = CONVERSION[menu_select]
            input_number = input("\nEnter the number to convert: ")
            input_check = number_check(input_number)
            if 1 == input_check:
                input_number = float(input_number)
                try:
                    output_number = convert_func(input_number)
                    print(f"{input_number} {in_unit} "
                          f"is {output_number:.4f} {out_unit}")
                except Exception as error:
                    print(f"Calculation error: {error}")
            elif 2 == input_check: 
                print(f"{input_number} is not a valid number.")
            else: 
                print("An unknown error occurred.")
        else:
            print(f"\n{menu_select} is not an available menu option.")
            print("Please run the program again and select a menu number.")
    elif 2 == menu_check:
        print("\nAn invalid selection was made.")
        print("Please run the program again and select a menu number.")
    else: 
        print("\nAn unknown error occurred.")