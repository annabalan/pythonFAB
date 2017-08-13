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
