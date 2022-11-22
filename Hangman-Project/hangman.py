# Imports the random module from "Numeric and Mathematical Modules" from The Python Standard Library
import random

# Imports the variable "words" from the hangmanwordlist.py file
# File includes thousands of words
from hangmanwordlist import words

# Imports the string module for the alphabet variable
import string

# Function randoms a word from the wordlist until the word has no "-" or " " in it.
def valid_words(words):
    word = random.choice(words)
    while "-" or " " in words:
        word = random.choice(words)
        return word.upper()                 # returns word in uppercase

# Beginning of the hangman function
def hangman():
    word = valid_words(words)               # retrieves the word from the function above
    alphabet = set(string.ascii_uppercase)  # stores ASCII uppercase characters in the alphabet variable
    word_letters = set(word)                # stores letters(str) of the chosen word
    used_letters = set()                    # stores letters(str) from user input

    # Defines how many tries the user has
    lives = 7

    # Loops until the there are no more letters in word_letters or no more lives(tries) left
    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and following letters have been used: ", " ".join(used_letters))

        # If the letter is in used_letters it shows the character else it shows a dash
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        # Get's user input
        user_input = input("Enter a letter: ").upper()
        
        # If user_input is in the remainding alphabet it get's added to the used_letters
        # and removed from the word_letters (the characters which needs to be guessed) 
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)

            # If user_input is in the remainding word_letters, it wil be removed from it
            if user_input in word_letters:
                word_letters.remove(user_input)
            
            # If user_input is not in word_letters set, then it remove a life/try
            else:
                lives -= 1     # same as lives = lives - 1
                print("Letter is not in the word. ")
        
        # If user_input already exists in used_letters it will print that it already has been used.
        elif user_input in used_letters:
            print("The character has already been used. ")

        # Else if the other conditions doesn't apply, it is an invalid character and it will print it out.
        else:
            print("Invalid character. Enter a valid character: ")

    # If the lives variable reaches 0, then the while-loop will stop
    # user get's the print message that he lost and what the word was.
    if lives == 0:
        print("You died. The word was", word)
    
    # Else the word_letters variable reached 0, which means all characters has been guessed.
    # Print will show that the user won and what the word was.
    print("You won. The word was", word, "!")

# hangman function get's called
hangman()
