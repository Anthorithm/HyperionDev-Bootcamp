# Correcting the errors and improving the code

# Syntax Error: Fixed print statements
print("Welcome to the error program")
print("\n")

# Logical Error: Fixed the assignment and Runtime Error: Removed non-numeric characters for casting
age_Str = "24"
age = int(age_Str) 
# Syntax Error: Fixed concatenation by converting int to str
print("I'm " + str(age) + " years old.")

# Logical Error: Fixed string to int conversion for arithmetic operation
years_from_now = 3
total_years = age + years_from_now
# Fixed print statement to correctly display the total years
print("The total number of years: " + str(total_years))

# Logical Error: Fixed the undefined variable and included 6 additional months in the calculation
# Also corrected the calculation to account for the additional 6 months
total_months = total_years * 12 + 6
# Syntax Error: Fixed concatenation by converting int to str
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old.")
