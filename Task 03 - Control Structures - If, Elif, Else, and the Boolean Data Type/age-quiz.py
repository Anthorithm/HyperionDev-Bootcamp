""" (age-quiz.py) This script prompts the user to enter their age and provides a corresponding message based on their age group.
It demonstrates basic error handling by ensuring that the user enters a valid integer for their age input. """

# Infinite loop to continuously prompt the user for input until a valid integer is entered
while True:
    # Prompt the user to enter their age
    age_string = input("Enter your age: ")

    try:
        # Attempt to convert the user input to an integer
        age = int(age_string)
        
        # Break out of the loop if input is successfully converted to an integer
        break  

    except ValueError:
        # If input cannot be converted to an integer, print an error message
        print("Invalid input! Please enter a valid integer for your age.")

# Once a valid integer is obtained, check conditions and output messages
if age >= 100:
    # Output message for ages 100 and above
    print("Sorry, you're dead.")
elif age >= 65:
    # Output message for ages 65 to 99
    print("Enjoy your retirement!")
elif age >= 40:
    # Output message for ages 40 to 64
    print("You're over the hill.")
elif age < 13:
    # Output message for ages 12 and below
    print("You qualify for the kiddie discount.")
elif age == 21:
    # Output message for age 21
    print("Congrats on your 21st!")
else:
    # Output message for all other ages
    print("Age is but a number.")
    