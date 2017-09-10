# Word Jumble
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

WORDS = ("python", "jumble", "book", "snack", "music", "sheet", "easy", "difficult", "answer", "xylophone")

# pick one word randomly from the sequence
word = random.choice(WORDS)

# create a variable to later use if the guess is correct
correct = word

# create an empty jumbled version of the word
jumble =""

while word:
  position = random.randrange(len(word))
  jumble += word[position]
  word = word[:position] + word[(position + 1):]
tries = 0
# start the game
print(
"""
        Welcome to Word Jumble!

    Unscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
    """
)
print("The jumble is:", jumble)
# add in hint and scoring
guess = input("\nYour guess: ")
while guess != correct and guess != "":
  print("Sorry, that's not it.")
  guess = input("Your guess, type hint for some help: ")

  while guess == "hint":
    if correct == "python":
        print("Snake or a language.")
    elif correct == "jumble":
        print("Pile")
    elif correct == "easy":
        print("Simple")
    elif correct == "difficult":
        print("Challenge.")
    elif correct == "answer":
        print("Response")
    elif correct == "xylophone":
        print("Music")
    tries += 1
    hints = 5 - tries
    guess = input("Your guess: ")

if guess == correct:
  print("That's it! You guessed it!\n")
  print("And you did it with", tries, "hints. That is", hints, "points.")
print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
