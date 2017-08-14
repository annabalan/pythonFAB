# Geek Translator
# Demonstrates using dictionaries.

geek = ["404": "clueless. From the web error message 404, meaning page not found.",
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
