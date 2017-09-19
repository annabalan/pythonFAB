# Character Creator Program

attributes = {"STRENGTH":"", "HEALTH":"", "WISDOM":"", "DEXTERITY":""}
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
  add = input("What attribute would you like to add points to?: ")
  if add in attributes:
      pts = input("\nHow many points would you like to add? ")
      attributes[add] = pts
      print("\n", add, "now has", pts)
  else:
      ("Sorry, but", add, "isn't a valid attriute.")
elif choice == "3":
    change = input("What attribute would you like to change points to?: ")
    if change in attributes:
        pts = input("What points would you like to add instead?: ")
        attributes[change] = pts
        print("\n", change, "now has", pts)
else:
  print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")
