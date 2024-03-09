# Loop over a range of numbers from 1 to 9
# 'i' will take on each value in this range during the loop
for i in range(1, 10):
    # Determine the number of stars for each row
    # For the first 5 rows, the number of stars equals the row number (i)
    # For rows 6 to 9, the number of stars decreases from 4 to 1
    # This creates a pattern where the maximum number of stars (5) is in the middle row
    num_stars = i if i <= 5 else 10 - i
    
    # Print the stars for the current row
    # '*' is multiplied by 'num_stars' to create a string with the required number of stars
    print('*' * num_stars)
