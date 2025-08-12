# Write your code here.
score = input("please type your score: ")
with open("score.txt", "a") as file:
    file.write(score + "\n")