# Finicky Counter
# Demonstrates using the break statements to exit a loop
# and the continue statements to jump back to the top of a loop

count = 0

while True:
    count += 1

# end loop if count greater than 10
    if count > 10:
        break

# skip 5
    if count == 5:
        continue

print(count)

input("\n\nPress the enter key to exit.")
