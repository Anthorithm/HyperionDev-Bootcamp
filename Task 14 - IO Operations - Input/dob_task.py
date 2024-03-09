""" (dob_task.py) This Python script reads data from a file named 'DOB.txt' which contains names and birthdates.
It separates the names and birthdates, and prints them in two distinct sections: 'Name' and 'Birthdate'.
Each name and birthdate is printed on a separate line under its respective section. """

# Open the file 'DOB.txt' in read mode
with open('DOB.txt', 'r') as file:
    # Read all lines from the file and store them in a list
    lines = file.readlines()

# Initialise a list to store names
names = []
# Initialise a list to store birthdates
birthdates = []

# Process each line from the file
for line in lines:
    # Split the line into parts, separating the name and birthdate
    parts = line.strip().rsplit(' ', 3)
    # Join the first parts as the name
    name = ' '.join(parts[:-3])
    # Join the last three parts as the birthdate
    birthdate = ' '.join(parts[-3:])
    # Add the name to the names list
    names.append(name)
    # Add the birthdate to the birthdates list
    birthdates.append(birthdate)

# Print the 'Name' section header
print("Names:")
# Print each name on a new line
for name in names:
    print(name)

# Print a newline for separation
print("\nBirthdates:")
# Print each birthdate on a new line
for birthdate in birthdates:
    print(birthdate)
