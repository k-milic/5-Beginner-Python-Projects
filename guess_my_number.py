# Imports the random module from "Numeric and Mathematical Modules" from The Python Standard Library
import random

# Input number will be turned
my_number = int(input("Enter your number (0-1000): "))

# Variable holds list wich will be used in the function below
options = ["1 - Higher", "2 - Lower"]


# Defining function
def pc_guess():
    # Variables need to be defined first before they can be referenced
    pc_guess = random.randint(0, 1000)
    low = -1        # get's overwritten with every loop
    high = 1001     # get's overwritten with every loop
    # Loops function until pc guesses the right number
    while pc_guess != my_number:
        print(pc_guess)
        # For is used to list the elements on each line for better readability
        for elements in options:
                print(elements)
        selected_option = int(input("My number is "))
        if selected_option == 1:
                low = pc_guess
                pc_guess = random.randint(low, high)
        elif selected_option == 2:
                high = pc_guess
                pc_guess = random.randint(low, high)
        
    print(f"The PC guessed your number. The number was {pc_guess}")
        
# Calls the defined function above
pc_guess()