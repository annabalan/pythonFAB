# Tip Calculator

bill_total = float(input("Enter Bill Total: "))


b15 = float("0.15")
b20 = float("0.20")

bill15 = bill_total * b15 + bill_total

bill20 = bill_total * b20 + bill_total

print("If you would like to leave a 15 percent tip, the total would be: ")
print(bill15)

print("Or if you would like to leave a 20 percent tip, the total would be: ")
print(bill20)

input("\n\nPress the enter key to exit.")
