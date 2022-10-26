# string concatenation (aka how to put string together)
# suppose we want to create a string that says "subscribe to _______"
# youtuber = "Name" # some string to variable

# a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")


# Defining all variables which will be used used in the madlib
adj1 = input("Add an adjective: ")
adj2 = input("Add another adjective: ")
verb1 = input("Add an verb: ")
verb2 = input("Add another verb: ")
verb3 = input("Add another verb: ")
verb4 = input("Add another verb: ")
famous_person = input("Add a name of a famous person: ")
noun1 = input("Add a noun: ")

# the madlib variable is holding all the strings with the variables defined above
madlib = f"Computer programming is so {adj1}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}! Somtimes I \
{verb3} about {adj2} {noun1} and wonder, what if I just {verb4} it?"

# prints out the madlib variable
print(madlib)