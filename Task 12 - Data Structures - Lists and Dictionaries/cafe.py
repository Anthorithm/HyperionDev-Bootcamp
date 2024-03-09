""" (cafe.py) This script is designed for a cafe's inventory management. It creates a list of menu items sold in the cafe, 
along with dictionaries for stock quantities and prices for each item. The script calculates the total worth 
of stock available in the cafe by multiplying the stock quantity by the price for each item. This is useful for 
keeping track of the value of goods in the cafe and for basic inventory management. """
    

# Creating a list called 'menu' with four items sold in the cafe
menu = ["Coffee", "Tea", "Sandwich", "Cake"]

# Creating a dictionary 'stock', containing the stock value for each menu item
stock = {
    "Coffee": 100,  # stock of Coffee
    "Tea": 200,     # stock of Tea
    "Sandwich": 50, # stock of Sandwich
    "Cake": 30      # stock of Cake
}

# Creating another dictionary 'price', containing the prices for each menu item
price = {
    "Coffee": 2.5,  # price of Coffee
    "Tea": 2.0,     # price of Tea
    "Sandwich": 5.0,# price of Sandwich
    "Cake": 4.0     # price of Cake
}

# Initialising a variable to calculate the total stock worth in the cafe
total_stock_worth = 0

# Looping through each item in the menu
for item in menu:
    # Calculating the value of each item (stock value * price)
    item_value = stock[item] * price[item]
    # Adding the item's value to the total stock worth
    total_stock_worth += item_value

# Printing the total stock worth
print("Total stock worth in the cafe: $", total_stock_worth)


