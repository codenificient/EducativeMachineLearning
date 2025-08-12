with open("message.txt", "w") as file:
    file.write("Hello from Python!")

with open("message.txt", "a") as file:
    file.write("\nAnother line!")
    
with open("message.txt", "r") as file:
    content = file.read()
    print(content)