totals = 0
while True:
    item = input("Enter an item (or 'done' to finish): ")
    if item == "done":
        with open("expenses.txt", "a") as file:
            file.write("TOTALS: $" + str(totals) + "\n")
        break
    amount = input("How much did you spend on it? ")
    totals += int(amount)
    with open("expenses.txt", "a") as file:
        file.write(item + ": $" + amount + "\n")  # Concatenate the strings before writing

print("All expenses saved!")
