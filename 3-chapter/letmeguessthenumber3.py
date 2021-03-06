# Let Me Guess The Number
# The player picks a random number between 1 and 100
# The computer tries to guess it and the player lets
# the computer know if the guess is too high, too low
# or right on the money

import random

print("\tWelcome to 'Let Me Guess The Number' !")
print("\nThink of a number between 1 and 100.")
print("I will try to guess it in as few attempts as possible.\n")

# set the initial values
print("Think of a Number, and I will guess!\n")
input("\nPress Enter when you've picked the number...")
SP = 1
EP = 100
guess = random.randint(SP, EP)
print("Is it...", guess, "?\n")
tries = 1
response = ""
response = input("Is it Lower, Higher or Right On: ")

while response != "Right On":
    if response == "Lower":
        EP = guess
        guess -= 1
        guess = random.randint(SP, EP)
        print ("I'll take another guess...", guess)
    elif response == "Higher":
        SP = guess
        guess += 1
        guess = random.randint(SP, EP)
        print ("I'll take another guess...", guess)
    elif response == "Right On":
        break
    response = input("Is it Lower, Higher or Right On: ")
    tries += 1

print("\nI guessed it!!!")
print("And it only took me", tries, "tries!\n")

input("\n\nPress the enter key to exit.")
