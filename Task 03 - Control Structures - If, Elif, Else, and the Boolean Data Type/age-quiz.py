# Get user input for age
age_string = input("Enter your age: ")

# Check if the input is numeric
if age_string.isdigit():
# Convert age input to an integer
    age = int(age_string)

# Check conditions and output messages
if age >= 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number.")
