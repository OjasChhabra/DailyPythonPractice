# Q — Temperature Ladder
# Accept temperature in °C and print a description.
# Input: -5 --Freezing Cold 🥶
# Input: 25 --Pleasant 😊
# Input: 45 ==Very Hot 🔥

temp = int(input("Enter the Temprature(in °C): "))
if temp <= 5:
    print("Freezing Cold 🥶")
elif temp <= 18:
    print("Cold 😬")
elif temp <= 25:
    print("Pleasant 😊")
elif temp <= 35:
    print("Hot 🥵")
elif temp > 35:
    print("Flammin Hot 🔥")
