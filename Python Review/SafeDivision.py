# Write your code here.
num1 = input("Enter a first number:")
num2 = input("Enter a second number:")

try:
    print(num1, "divided by", num2, "equals", int(num1) / int(num2))
except:
    print("Sorry, cannot divide by Zero")