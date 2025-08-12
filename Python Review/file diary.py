entry = input("Write a diary entry: ")

with open("diary.txt", "a") as file:
    file.write(entry + "\n")