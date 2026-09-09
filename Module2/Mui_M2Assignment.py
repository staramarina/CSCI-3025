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
slicedstring1 = string1[12:17]                              #slice string1 to isolate "Python"
slicedstring2 = stringjoin1[25:29]                          #slice stringjoin1 to isolate "fun!"
stringjoin2 = slicedstring1 + " is " + slicedstring2        #join sliced strings with " is " in between

#boolean expressions
bool1 = num4 > num3             #check if num4 is greater than num3, should be true
bool2 = len(stringjoin1) >= 28  #check if the length of stringjoin1 is greater than or equal to 28, should be true

#output statements
