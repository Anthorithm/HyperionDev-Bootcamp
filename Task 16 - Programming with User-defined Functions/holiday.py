"""
This Python script calculates the total cost of a holiday based on user inputs for flight destination, 
number of hotel nights, and car rental days. It includes functions for calculating costs of each aspect 
of the holiday (hotel, plane, car rental) and validates user input to ensure the city name does not contain 
numbers. The script aims to provide a detailed breakdown of holiday costs to aid in planning and budgeting.

Purpose:
- To assist users in estimating the total cost of their holiday.
- To demonstrate basic Python programming concepts such as functions, conditionals, and user input validation.
"""
# Define a function to calculate the hotel cost based on the number of nights.
def hotel_cost(num_nights):
    price_per_night = 100  # Set price per night.
    return num_nights * price_per_night  # Calculate total cost.

# Define a function to calculate the plane cost based on the destination city.
def plane_cost(city_flight):
    # Determine flight cost based on city.
    if city_flight.lower() == "paris":
        return 200
    elif city_flight.lower() == "london":
        return 250
    elif city_flight.lower() == "new york":
        return 300
    else:
        return 150  # Default cost for other cities.

# Define a function for calculating car rental cost based on the number of rental days.
def car_rental(rental_days):
    daily_rental_cost = 40  # Set daily rental cost.
    return rental_days * daily_rental_cost  # Calculate total rental cost.

# Define a function to calculate the total holiday cost.
def holiday_cost(city_flight, num_nights, rental_days):
    hotel = hotel_cost(num_nights)  # Calculate hotel cost.
    plane = plane_cost(city_flight)  # Calculate plane cost.
    car = car_rental(rental_days)  # Calculate car rental cost.
    total = hotel + plane + car  # Sum up total costs.
    # Print individual costs.
    print(f"Hotel cost for {num_nights} nights: £{hotel}")
    print(f"Plane cost for flying to {city_flight}: £{plane}")
    print(f"Car rental cost for {rental_days} days: £{car}")
    # Print the total holiday cost.
    print(f"Which adds up to a total cost of: £{total}")
    return total

# Check if the city input is valid (contains only letters).
def is_input_valid(city):
    return city.isalpha()  # True if all characters in city are alphabetic.

# Get user input for the city, validating to ensure no numbers are included.
city_flight = input("Enter the city you will be flying to: ")
while not is_input_valid(city_flight):  # Repeat until a valid city is entered.
    print("Please enter a valid city name without any numbers.")
    city_flight = input("Enter the city you will be flying to: ")

# Get user input for the number of hotel nights and car rental days.
num_nights = int(input("Enter the number of nights you will be staying at the hotel: "))
rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

# Calculate and print the detailed holiday cost using the user's inputs.
holiday_cost(city_flight, num_nights, rental_days)
