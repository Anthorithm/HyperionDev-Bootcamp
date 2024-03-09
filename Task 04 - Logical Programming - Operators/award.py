# Get times for swimming, cycling, and running events
# The user is prompted to input their times in minutes for each event
swimming_time = float(input("Enter swimming time (in minutes): "))
cycling_time = float(input("Enter cycling time (in minutes): "))
running_time = float(input("Enter running time (in minutes): "))

# Calculate total time for the triathlon by summing the individual times
# This total time is the sum of swimming, cycling, and running event times
total_time = swimming_time + cycling_time + running_time

# Determine the award based on the total time
# The award category is decided based on how the total time compares to preset benchmarks
if total_time <= 100:
    award = "Provincial Colours"  # Awarded if total time is 100 minutes or less
elif total_time <= 105:
    award = "Provincial Half Colours"  # Awarded if total time is between 101 and 105 minutes
elif total_time <= 110:
    award = "Provincial Scroll"  # Awarded if total time is between 106 and 110 minutes
else:
    award = "No award"  # No award is given if the total time exceeds 110 minutes

# Display the result
# The total time and the corresponding award are printed for the user
print(f"\nTotal time taken to complete the triathlon: {total_time} minutes")
print("Award: " + award)
