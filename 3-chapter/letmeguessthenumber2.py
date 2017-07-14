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
number = int(input("Choose a Number: "))

guess = random.randint(1, 100)
tries = 1
print("I'm taking a guess...", guess)

response = ""
response = input("Is it Lower or Higher: ")

while guess != number:
    if guess > number:
        guess -= 1
        guess = random.randint(1, guess)
    else:
        guess += 1
        guess = random.randint(guess, 100)
        print ("I'll take another guess...", guess)
        response = input("Is it Lower or Higher: ")
    tries += 1


print("I guessed it! The number was", number)
print("And it only took me", tries, "tries!\n")

input("\n\nPress the enter key to exit.")
