# Who's Your Daddy

print("\t\t\tWho's Your Daddy?")

father_son = {"Bobby Adams": "Mike Adams", "Jim Adduci": "Sandy Alomar",
"Sandy Alomar Jr.": "Felipe Alou", "Moises Alou": "Ruben Amaro", "Ruben Amaro Jr": "Angel Aragon",
"Tony Armas": "Tony Armas, Jr."}

choice = None
while choice != "0":
  print(
  """
  Who's Your Daddy

  0 - Quit
  1 - Look up an Entry
  2 - Add an Entry
  3 - Delete a Entry
  """
  )
  choice = input("Choice: ")
  print()
  # exit
  if choice == "0":
    print("Good-bye.")
  elif choice == "1":
    entry = input("Enter the Son's name: ")
    if entry in father_son:
        father = father_son[entry]
        print("\n", father)
    else:
        print("\nSorry, that name is information is not on file.")
  elif choice == "2":
      entry = input("What is the son's name?: ")
      if entry not in father_son:
          father = input("\nWho's the father?: ")
          father_son[entry] = father
          print("\n", entry, "has been added.")
      else:
          print("\nThat name already exists! Try another.")
    # delete a term-definition pair
  elif choice == "3":
      entry = input("What name do you want me to delete?: ")
      if entry in father_son:
        del father_son[entry]
        print("\nOkay, I deleted", entry)
      else:
        print("\nI can't do that!", entry, "doesn't exist.")
  else:
      print("\nSorry, but", choice, "isn't a valid choice.")
  input("\n\nPress the enter key to exit.")
