# Character Creator Program

attributes = ("Strength":"", "Health":"", "Wisdom":"", "Dexterity":"")
print("\t\tWelcome to Character!")
print("You have 30 points that you can use for any of these characters.")
print("You can spend it on,", attributes)

points = 30
print(
"""
0 - Exit
1 - Show Point Pool
2 - Add Points To a Character
3 - Return Points Back To The Pool
""")
choice = input("Choice: ")
print()
# exit
if choice == "0":
  print("Good-bye.")
elif choice == "1":
  print("Point Pool\n",points)
elif choice == "2":
  ch = int(input("What character would you like to add points to?:"))
  pts = int(input("How many points would you like to add?: "))
  entry = (ch.pts)
else:
  print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")
