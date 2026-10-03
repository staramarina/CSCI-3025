# Tiffany M. Mui
# Module 4 Assignment
# CSCI-3025: Python Programming
# Purpose: Demonstrate functions and handling errors
# Sources: NIST. (2024). SP 365: Metric Conversion Card. 
#     https://doi.org/10.6028/NIST.SP.365-2024


def input_menu():
    """Prints user input options and returns user input"""
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


if __name__ == "__main__":
    print("Select the number corresponding to the input unit (or q to quit)")
    InputUnit = input_menu()
    print(InputUnit)