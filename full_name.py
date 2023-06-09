
# This program will be used to validate that a user inputs at least two names when asked to enter their full name.
# Perform some validation to check that the user has entered a full name. Give an appropriate error message if they haven’t. 
# Ask the user to input their full name 
name  = input(str("Please enter your full name :"))

# Using len() fuction we can see how many caracters the user input. In order to have a full name we need at least 4 characters and max of 25 characters.
# If the user haven't type anything the message will be : You haven’t entered anything. Please enter your full name.”
if len(name) == 0 :
    print("You haven't entered anything. Please enter your full name.")


# If the user enter less than 4 characters the message will be : “You have entered less than 4 characters. Please make sure that you have entered your name and surname.”
elif len(name) < 4 :
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surmane.")


# If the user enter more than 25 characters the message will be :“You have entered more than 25 characters. Please make sure that you have only entered your full name.”
elif len(name) > 25 :
    print("You have entered more than 25 characters. Please make sure that you have only enter your full name.")


# If the user enter between 4 and 25 characters the message will be :“Thank you for entering your name.”
else :
    print("Thank you for entering your name.")