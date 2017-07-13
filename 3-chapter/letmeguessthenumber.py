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
SP = 1
ED = 100
guess = random.randint(SP, ED)
number = int(input("Choose a Number: "))

print(guess)

response = input("Is it Lower or Higher: ")

while guess != number:
    if response == "Lower":
        guess = random.randit(1, guess)
    elif response == "Higher":
        guess = random.randint(guess, 100)
    else:
        print("Try Again")

        response = input("Is it Lower or Higher: ")

print("I guessed it! The number was", the_number)

input("\n\nPress the enter key to exit.")
