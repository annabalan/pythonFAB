# Hangman Game
#
# The classic game of Hangman. The computer picks a random word
# and the player wrong to guess it, one letter at a time. If the player
# can't guess the word in time, the little stick figure gets hanged.

# imports
import random
# constants
HANGMAN = (
"""
   +---+
   |   |
       |
       |
       |
       |
 =========
 """,
 """
    +---+
    |   |
    O   |
        |
        |
        |
 =========
 """,
 """
    +---+
    |   |
    O   |
    |   |
        |
        |
 =========
 """,
 """
     +---+
     |   |
     O   |
    /|   |
         |
         |
  =========
  """,
  """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
   =========
   """,
   """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
   =========
   """,
   """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
   =========
   """)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED", "TEA", "PIANO", "BLANKET", "CLAM", "GUAM", "TAFFETA", "PYTHON", "FILM", "DEADLY", "BOOK", "ROYAL", "COLUMN", "BED", "MOUNTAIN")
# initialize variables
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

print("Welcome to Hangman. Good luck!")

while (wrong < MAX_WRONG) and (so_far != word):
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while (guess in used):
        print ("You've already guessed the letter:", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()

    used.append(guess)

    if (guess in word):
        print ("\nYes!", guess, "is in the word!")

        # create a new so_far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1

if (wrong == MAX_WRONG):
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")

print("\nThe word was", word)
input("\nPress the enter key to exit.")
