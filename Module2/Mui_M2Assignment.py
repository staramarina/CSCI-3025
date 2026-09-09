# Tiffany M. Mui
# Module 2 Assignment
# CSCI-3025: Python Programming
# Purpose: Demonstrate variables, data types, and expressions in Python

#define variables
num1 = 11
num2 = 7
num3 = 3.14
num4 = 5.39
string1 = "Let's learn Python!"

#arithmetic operations
sum23 = num2 + num3             #summation of integer and decimal type
product13 = num1 * num3         #multiplication of integer and decimal type
difference24 = num2 - num4      #subtraction of integer and decimal type
quotient12 = num1 / num2        #division of integers
quotient14 = num1 / num4        #division of integer and decimal type
quotient43 = num4 / num3        #division of decimal types

#string manipulations
stringjoin1 = ' '.join([string1, "It's fun!"])              #add another string to the end of string1 with a space between strings
slicedstring1 = string1[12:18]                              #slice string1 to isolate "Python"
slicedstring2 = stringjoin1[25:29]                          #slice stringjoin1 to isolate "fun!"
stringjoin2 = slicedstring1 + " is " + slicedstring2        #join sliced strings with " is " in between

#boolean expressions
bool1 = num4 > num3             #check if num4 is greater than num3, should be true
bool2 = len(stringjoin1) >= 28  #check if the length of stringjoin1 is greater than or equal to 28, should be true

#output statements
print("\nArithmetic operations included:")
print("Summation of integer", num2, "and decimal", num3, "results in the sum", sum23)
print("Multiplication of integer", num1, "and decimal", num3, "results in the product", product13)
print("Subtraction of decimal", num4, "from integer", num2, "results in the difference", difference24)
print("Division of integer", num1, "by integer", num2, "results in quotient", quotient12)
print("Division of integer", num1, "by decimal", num4, "results in quotient", quotient14)
print("Division of decimal", num4, "by decimal", num3, "results in quotient", quotient43)
print("Note that arithmetic operations between integers and decimals may not behave as expected.")
print("\nString manipulations included:")
print(f"Joining string '{string1}' with 'It's fun!' results in '{stringjoin1}'")
print(f"Slicing '{string1}' from position 12 to 18 results in '{slicedstring1}'")
print(f"Slicing the joined string '{stringjoin1}' from position 25 to 29 results in {slicedstring2}")
print(f"Combining the sliced strings with 'is' in the center results in '{stringjoin2}'")
print("\nBoolean expressions included")
print(f"Testing whether {num4} is greater than {num3} with the result {bool1}")
print(f"Testing whether the length of '{stringjoin1}' exceeds a character limit of 28 with the result being {bool2}\n")