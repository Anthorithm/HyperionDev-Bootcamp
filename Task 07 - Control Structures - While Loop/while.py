""" (while.py) This script continually prompts the user to enter numbers until the user enters -1.
It then calculates and displays the average of all entered numbers, excluding the -1.
The script uses a while loop for repeated prompting and input collection. """

# Set a list to store the numbers entered by the user
numbers = []

# Start a loop that will run indefinitely
while True:
    # Ask the user to enter a number
    user_input = input("Enter a number (or -1 to stop): ")
    
    # Try to convert the input to an integer
    try:
        number = int(user_input)
    except ValueError:
        # If conversion fails, print an error message and continue to the next iteration
        print("Please enter a valid number.")
        continue

    # Check if the user entered -1; if so, break out of the loop
    if number == -1:
        break
    else:
        # If the number is not -1, add it to the list
        numbers.append(number)

# Check if any numbers were entered (list is not empty)
if numbers:
    # Calculate the average of the numbers by dividing the sum by the number of items
    average = sum(numbers) / len(numbers)
    # Print the calculated average
    print("The average of the numbers entered is:", average)
else:
    # If no numbers were entered (list is empty), print a message
    print("No numbers were entered.")

