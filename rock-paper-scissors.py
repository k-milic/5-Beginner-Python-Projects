# Imports the random module from "Numeric and Mathematical Modules" from The Python Standard Library
import random
print("ROCK, PAPER, SCISSORS")

# Defining the play function
def play():
    # Getting the user input and turning string into lowercase
    user = input("Choose [R]ock, [P]aper or [S]cissors: ").lower()

    # Displaying what the user have chosen
    if user == "r":
        print("You chose rock.")
    if user == "p":
        print("You chose paper. ")
    if user == "s":
        print("You chose scissors")

    # Displaying what the computer has generated or chosen from the list of r, p and s
    computer = random.choice(["r", "p", "s"])
    if computer == "r":
        print("Computer chose rock.")
    if computer == "p":
        print("Computer chose paper. ")
    if computer == "s":
        print("Computer chose scissors")

    # If user and computer input is equal it returns the string "It's a tie!"
    if user == computer:
        return "It's a tie!"
    
    # Calls the fun_win function with the user and computer argument.
    # user argument replaces player parameter and computer argument replaces opponent parameter
    if fun_win(user, computer):
        return "YOU HAVE WON! "
    
    # If the other 2 if-statements are not met, this will get called by default
    # saves unnecessary line of code
    return "You have lost. "

# Defines the win condition
def fun_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") \
        or (player == "s" and opponent == "p"):
        return True

print(play())

# User gets prompted if he wants to play again
play_again = input("Do you want to play again? (y/n): ").lower()

# Function get's recalled until the user enters "n"
while play_again != "n":
    print(play())
    play_again = input("Do you want to play again? (y/n): ").lower()

