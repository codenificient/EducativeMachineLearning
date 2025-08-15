while True:
    item = input("Enter an item (or 'done' to finish): ")
    if item == "done":
        break
    amount = input("How much did you spend on it? ")
    with open("expenses.txt", "a") as file:
        file.write(item + ": $" + amount + "\n")

with open("expenses.txt", "r") as file:
    print("Here are your expenses:")
    print(file.read())
	