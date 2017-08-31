# random words
# print all words from a list in a random order without repeating

import random

words = ["copper", "explain", "ill-fated", "truck", "neat", "unite", "branch", "educated",
"tenuous", "hum", "decisive", "notice"]

while words != 0:
  high = len(words)
  low =  0
  random_word = random.randrange(low, high)
  print(words[random_word])
  del(words[random_word])

input("\nPress enter to exit.")
