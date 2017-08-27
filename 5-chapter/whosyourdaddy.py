# Who's Your Daddy

print("\t\t\tWho's Your Daddy?")

father_son = ["Bobby Adams" : "Mike Adams", "Jim Adduci" : "Sandy Alomar",
"Sandy Alomar Jr." : "Felipe Alou", "Moises Alou" : "Ruben Amaro", "Ruben Amaro Jr" : "Angel Aragon",
"Tony Armas" : "Tony Armas, Jr."]

choice = None
while choice != "0":
  print(
  """
  Who's Your Daddy

  0 - Quit
  1 - Look up a Father-Son
  2 - Add a Father-Son
  3 - Delete a Geek Term
  """
  )
  choice = input("Choice: ")
  print()
  # exit
  if choice == "0":
    print("Good-bye.")
  elif choice == "1":
    term = input("Enter the son's name: ")
    if term in father_son:
        print("\n", term)
    else:
        print("\nSorry, that name is inforation is not on file.")
  elif choice == "2":
      term = input("What is the son's name?: ")
      if term not in father_son:
          definition = input("\nWho's the father?: ")
          father_son[term] = definition
          print("\n", term, "has been added.")
      else:
          print("\nThat name already exists! Try another.")
    # delete a term-definition pair
elif choice == "3":
      term = input("What name do you want me to delete?: ")
      if term in father_son:
        del father_son[term]
        print("\nOkay, I deleted", term)
      else:
        print("\nI can't do that!", term, "doesn't exist.")
    else:
      print("\nSorry, but", choice, "isn't a valid choice.")
  input("\n\nPress the enter key to exit.")
