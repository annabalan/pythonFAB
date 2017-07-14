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
a = 1
b = 100
guess = random.randint(a, b)
number = int(input("Choose a Number: "))
tries = 1
print(guess)

response = ""
response = input("Is it Lower or Higher: ")

while guess != number:
    if response == "Lower":
        a = 1
        b = guess
        guess = random.randint(a, b)
        print(guess)
    elif response == "Higher":
        a = guess
        b = 100
        guess = random.randint(a, b)
        print(guess)
    guess = random.randint(a, b)
    response = input("Is it Lower or Higher: ")
    tries += 1


print("I guessed it! The number was", number)
print("And it only took me", tries, "tries!\n")

input("\n\nPress the enter key to exit.")
