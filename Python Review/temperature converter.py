# Modidy the code below to let the users convert multiple temperatures in one run and log the results in a list. 
# At the end, print all conversions done during the session.
print("🌡️ Welcome to the Temperature Converter!")
print("Choose a conversion:")
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")
print("3: Celsius to Kelvin")
print("4: Kelvin to Celsius")
print("5: Fahrenheit to Kelvin")
print("6: Kelvin to Fahrenheit")
choice = input("Enter your choice (1-6): ")
temp = float(input("Enter the temperature to convert: "))
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


if choice == "1":
    result = celsius_to_fahrenheit(temp)
    print("{}°C is {:.2f}°F".format(temp, result))
elif choice == "2":
    result = fahrenheit_to_celsius(temp)
    print("{}°F is {:.2f}°C".format(temp, result))
elif choice == "3":
    result = celsius_to_kelvin(temp)
    print("{}°C is {:.2f}K".format(temp, result))
elif choice == "4":
    result = kelvin_to_celsius(temp)
    print("{}K is {:.2f}°C".format(temp, result))
elif choice == "5":
    result = fahrenheit_to_kelvin(temp)
    print("{}°F is {:.2f}K".format(temp, result))
elif choice == "6":
    result = kelvin_to_fahrenheit(temp)
    print("{}K is {:.2f}°F".format(temp, result))
else:
    print("Invalid choice. Please run the program again.")