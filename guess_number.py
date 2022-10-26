###############################
##### GUESSING THE NUMBER #####
###############################

# The computer is generating a random number
# and we need to guess this generated number.

# Imports the random module from "Numeric and Mathematical Modules" from The Python Standard Library
import random

# Getting the user input to define MAX and MIN range
print("Define the number range")
start_range = int(input("Enter lowest possible number: "))
max_range = int(input("Enter highest possible number: "))

# Defines guessing function
def guess():
    random_number = random.randint(start_range, max_range)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the Number between {start_range} and {max_range}: "))
        if guess < random_number:
            print("The number is higher")
        elif guess > random_number:
            print("The number is lower")
    print(f"YOU GUESS THE NUMBER! The number is: {random_number}")


# Calls the defined function above
guess()



