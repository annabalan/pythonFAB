# Fortune Cookie
print("\t\t'Welcome to The Fortune Cookie!\n")

import random

fortune = random.randint(1, 5)

print("Your fortune cookie is...")

if fortune == 1:
  print("He who laughs at himself never runs out of things to laugh at.")
elif fortune == 2:
  print("The greatest danger could be your stupidity.")
elif fortune == 3:
  print("It is a good day to have a good day.")
elif fortune == 4:
  print("Hard work pays off in the future. Laziness pays off now.")
elif fortune == 5:
  print("An alien of some sort will be appearing to you shortly.")

input("\n\nPress the enter key to exit")
