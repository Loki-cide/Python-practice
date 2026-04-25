import math

weight = float(input("Enter your weight: "))
unit = input("Is the weight in kilogram or pound(k/p): ")

if unit == "k":
    weigh = weight * 2.205
    unit = "kgs"
    print(f"Your weight in kilograms is {weigh} {unit}")
elif unit == "p":
    weigh = weight / 2.205
    unit = "lbs"
    print(f"YOur weight in pounds is {weigh} {unit}")
else:
    print(f"{unit} is not valid")