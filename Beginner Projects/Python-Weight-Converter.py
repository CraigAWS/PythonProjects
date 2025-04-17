# Pyhton Weight Converter

weight = float(input("Enter your weight: "))
unit = input("(K)g or (L)bs: ")

if unit == "K":
    weight = weight * 2.205
    print(f"Weight in Lbs: {round(weight, 1)}")
elif unit == "L":
    weight = weight / 2.205
    print(f"Weight in Kgs: {round(weight, 1)}")
else:
    print("Please enter a valid unit")