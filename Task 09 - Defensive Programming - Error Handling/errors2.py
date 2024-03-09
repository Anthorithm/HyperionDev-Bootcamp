# Corrected example program

# Fixed: Enclose string literals in quotes
animal = "Lion"
animal_type = "cub"

# Assuming the value is correct but the description was wrong in the original string
number_of_teeth = 16

# Fixed: Corrected string formatting with .format() method
# The placeholders {} are filled with the values of the variables
full_spec = "This is a {}. It is a {} and it has {} teeth".format(animal, animal_type, number_of_teeth)

# Fixed: Add parentheses for the print function (Python 3 syntax)
print(full_spec)
