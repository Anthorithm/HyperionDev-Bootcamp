

# Infinite loop to continuously prompt the user for input until a valid integer is entered
while True:
    
    age_string = input("Enter your age: ")

    try:
        
        age = int(age_string)
        
        break  

    except ValueError:
        
        print("Invalid input! Please enter a valid integer for your age.")

# Once a valid integer is obtained, check conditions and output messages
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
