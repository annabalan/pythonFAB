# Geek Translator
# Demonstrates using dictionaries.

geek = ["404" : "clueless. From the web error message 404, meaning page not found.",
"Googling": "searching the Internet for background information on a person.",
"Keyboard Plaque": "the collection of debris found in computer keyboards.",
"Link Rot": "the process by which web page links become obsolete.",
"Percussive Maintenace": "the act of striking an electronic device to make it work.",
"Uninstalled": "being fired. Especially popular during the dot-bomb era."]


choice = None
while choice != "0":
  print(
  """
  Geek Translator

  0 - Quit
  1 - Look up a Geek Term
  2 - Add a Geek Term
  3 - Redefine a Geek Term
  4 - Delete a Geek Term
  """
  )
  choice = input("Choice: ")
  print()
  # exit
  if choice == "0":
    print("Good-bye.")
  elif choice == "1":
    term = input("What term do you want me to translate?: ")
    if term in geek:
        definition = geek[term]
        print("\n", term, "means", definition)
    else:
        print("\nSorry, I don't know", term)
  elif choice == "2":
      term = input("What term do you want me to add?: ")
      if term not in geek:
          definition = input("\nWhat's the definition?: ")
          geek[term] = definition
          print("\n", term, "has been added.")
      else:
          print("\nThat term already exists! Try redefining it.")
# redifine an existing term
    elif choice == "3":
        term = input("What term do you want me to redifine?: ")
        if term in geek:
            definition = input("What's the new definiton?: ")
            geek[term] = definition
            print("\n", term, "has been redfinied.")
        else:
            print("\nThat term doesn't exists! Try adding it.")
