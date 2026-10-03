# Tiffany M. Mui
# Module 4 Assignment
# CSCI-3025: Python Programming
# Purpose: Demonstrate functions and handling errors
# Sources: NIST. (2024). SP 365: Metric Conversion Card. 
#     https://doi.org/10.6028/NIST.SP.365-2024


IN_CM = 2.54 # Inches to centimeter conversion ratio
MI_KM = 1.609344 # Miles to kilometers conversion ratio
LB_KG = 0.45359237 # Pounds to kilograms conversion ratio


def inch_to_cm(inch):
    """Convert inches to centimeters.
    
    Args:
        inch: Length in inches (must be numeric, can be negative)

    Returns: 
        cm: Length in centimeters

    Examples:
        >>> inch_to_cm(1)
        2.54
        >>> inch_to_cm(0)
        0.0
        >>> inch_to_cm(-1)
        -2.54
    """
    cm = inch * IN_CM
    return cm


def cm_to_inch(cm):
    """Convert centimeters to inches.
    
    Args:
        cm: Length in centimeters (must be numeric, can be negative)
    
    Returns:
        inch: Length in inches
    
    Examples: 
        >>> cm_to_inch(1)
        0.3937
        >>> cm_to_inch(0)
        0.0
        >>> cm_to_inch(-1)
        -0.3937
    """
    inch = cm / IN_CM
    return inch


def mile_to_km(mile):
    """Convert miles to kilometers.
    
    Args:
        mile: Length in miles (must be numeric, can be negative)
    
    Returns:
        km: Length in kilometers
    
    Examples:
        >>> mile_to_km(1)
        1.609344
        >>> mile_to_km(0)
        0.0
        >>> mile_to_km(-1)
        -1.609344
    """
    km = mile * MI_KM
    return km


def km_to_mile(km):
    """Convert kilometers to miles.
    
    Args:
        km: Length in kilometers (must be numeric, can be negative)
    
    Returns:
        mile: Length in miles
        
    Examples:
        >>> km_to_mile(1)
        0.62137
        >>> km_to_mile(0)
        0.0
        >>> km_to_mile(-1)
        -0.62137
    """
    mile = km / MI_KM
    return mile


def lb_to_kg(pound):
    """Convert pounds to kilograms.
    
    Args:
        pound: Mass/weight in pounds (must be numeric, can be negative)
    
    Returns:
        kg: Mass/weight in kilograms
    
    Examples:
        >>> lb_to_kg(1)
        0.45359237
        >>> lb_to_kg(0)
        0.0
        >>> lb_to_kg(-1)
        -0.45359237
    """
    kg = pound * LB_KG
    return kg


def kg_to_lb(kg):
    """Convert kilograms to pounds.
    
    Args:
        kg: Mass/weight in kilograms (must be numeric, can be negative)
    
    Returns:
        pound: Mass/weight in pounds
    
    Examples:
        >>> kg_to_lb(1)
        2.20462
        >>> kg_to_lb(0)
        0.0
        >>> kg_to_lb(-1)
        -2.20462
    """
    pound = kg / LB_KG
    return pound


def fah_to_cel(fah):
    """Convert degrees Fahrenheit to degrees Celsius.
    
    Args:
        fah: Temperature in Fahrenheit (must be numeric, can be negative)
    
    Returns:
        cel: Temperature in Celsius
    
    Examples:
        >>> fah_to_cel(32)
        0
        >>> fah_to_cel(0)
        -17.7778
        >>> fah_to_cel(-32)
        -35.5556
    """
    cel = (fah - 32) / 1.8
    return cel


def cel_to_fah(cel):
    """Convert degrees Celsius to degrees Fahrenheit.
    
    Args:
        cel: Temperature in Celsius (must be numeric, can be negative)
    
    Returns:
        fah: Temperature in Fahrenheit
        
    Examples:
        >>> cel_to_fah(32)
        89.6
        >>> cel_to_fah(0)
        32
        >>> cel_to_fah(-32)
        -25.6
    """
    fah = (cel * 1.8) + 32
    return fah

# ------------------------------------------------------------------------------
# CONVERSION: A dictionary that maps menu options to conversion functions
# Elements in the dictionary are 5-tuple using the following
#   [0]: conversion function - input float, return float
#   [1]: abbreviated input unit used for printing results
#   [2]: abbreviated output unit used for printing results
#   [3]: full input unit name used for menu display
# ------------------------------------------------------------------------------
CONVERSION = {
    1: (inch_to_cm, "in", "cm", "inches"),
    2: (mile_to_km, "mi", "km", "miles"),
    3: (cm_to_inch, "cm", "in", "centimeters"),
    4: (km_to_mile, "km", "mi", "kilometers"),
    5: (lb_to_kg, "lb", "kg", "pounds"),
    6: (kg_to_lb, "kg", "lb", "kilograms"),
    7: (fah_to_cel, "\N{DEGREE SIGN}F", "\N{DEGREE SIGN}C", "Fahrenheit"),
    8: (cel_to_fah, "\N{DEGREE SIGN}C", "\N{DEGREE SIGN}F", "Celsius"),
}


def menu_input_check(user_input = "No Input"):
    """Checks the format of user input from the selection menu.

    Args:
        user_input: menu option selection (default: "No Input")
    
    Returns:
        true if user_input is a valid integer, otherwise false.
    """
    try:
        int(user_input)
        return True
    except (ValueError, TypeError):
        return False


def print_menu():
    """Prints the menu options based on the conversion dictionary"""
    print("Select the number corresponding to the input unit (or q to quit)")
    for option, (_, short_unit, _, long_unit) in sorted(CONVERSION.items()):
        print(f"{option} -- {long_unit} ({short_unit})")
    print("q -- Quit")


def run_conversion(selection, func, u_in, u_out, long_in):
    """Perform the unit conversion and handle errors"""
    input_number = input("\nEnter the number to convert: ")
    try:
        input_number = float(input_number)
        output_number = func(input_number)
        print(f"{input_number} {u_in} is {output_number:.4f} {u_out}")
    except ValueError:
        print(f"{input_number} is not a valid number.")
    except ZeroDivisionError:
        print("Division by zero occurred during calculation.")
    except TypeError as error:
        print(f"Encountered type error: {error}")
    except Exception as error: 
        print(f"Encountered error: {error}")


if __name__ == "__main__":
    print_menu()
    menu_select = input()
    menu_check = menu_input_check(menu_select)
    while 'q' != menu_select:
        if menu_check:
            menu_select = int(menu_select)
            if menu_select in CONVERSION:
                func, in_u, out_u, in_long= CONVERSION[menu_select]
                run_conversion(menu_select, func, in_u, out_u, in_long)
            else:
                print(f"\n{menu_select} is not an available menu option.")
        else:
            print("\nAn invalid selection was made.")
        cont_flag = input("\nWould you like to convert another number? (y/n): ")
        if 'y' == cont_flag:
            print("\n")
            print_menu()
            menu_select = input()
            menu_check = menu_input_check(menu_select)
        else: 
            break
    print("\nThank you for using the unit conversion calculator!")