# Word Jumble
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

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

# start the game
print(
"""
        Welcome to Word Jumble!

    Unscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
    """
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
  print("Sorry, that's not it.")
  if word == "python":
      print("I might be a snake or a language.")
  elif word == "jumble":
      print("Pile of things.")
  elif word == "easy":
      print("This is simple.")
  elif word == "difficult":
      print("This ones hard.")
  elif word == "answer":
      print("Think of a question.")
  elif word =="xylophone":
      print("I'm related to music.")
  guess = input("Your guess: ")

if guess == correct:
  print("That's it! You guessed it!\n")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
