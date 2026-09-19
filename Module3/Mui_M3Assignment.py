# Tiffany M. Mui
# Module 2 Assignment
# CSCI-3025: Python Programming
# Purpose: Demonstrate conditional statements, for loops, and while loops

#Part 1: conditional structure to evaluate letter grade from a numerical score
score = input("Enter a percentage score (do not include '%'): ")                # prompt user to enter a score as a numerical value
tryagain = True                                                                 # try again flag used to determine whether loop should run again
while True == tryagain:                                                         # while loop to continue attempting to get correct user input
    try:                                                                        # try statement to check that user input is correct format
        score = float(score)                                                    # attempt to convert input value to a float type
        tryagain = False                                                        # attempt was successful, so set the try again flag to false
    except:                                                                     # exception handles when user input is not in correct format
        print("Error processing input, please try again.")                      # tells the operator that the input could not be processed
        score = input("Enter a percentage score (do not include '%'): ")        # attempt to get operator input again
if score >= 90.0:                                                               # if the score is greater than or equal to 90
    print(f"A score of {score}% results in grade A.")                           # print A grade and exit conditional statement
elif score >= 80:                                                               # if the score is greater than or equal to 80
    print(f"A score of {score}% results in grade B.")                           # print B grade and exit conditional statement
elif score >= 70:                                                               # if the score is greater than or equal to 70
    print(f"A score of {score}% results in grade C.")                           # print C grade and exit conditional statement
elif score >= 60:                                                               # if the score is greater than or equal to 60
    print(f"A score of {score}% results in grade D.")                           # print D grade and exit conditional statement
else:                                                                           # if the score is less than 60
    print(f"A score of {score}% results in grade F.")                           # print F grade and exit conditional statement

# Part 2: 
