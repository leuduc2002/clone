height = None
mass = None
while height is None or mass is None:
    try:
        height = float(input("Your height (cm): "))
        mass = float(input("Your mass (kg): "))
        if height <= 0 or mass <= 0:
            print("INVALID NUMBER")
            height = None
    except ValueError:
        print("syntax error")
height_2 = (height / 100) ** 2
BMI = mass / height_2
print("Your BMI:", round(BMI, 1))
youre = "You Are"
if BMI < 16:
    print(youre, "Severely Underweight")
elif BMI < 18.5:
    print(youre, "Underweight")
elif BMI < 25:
    print(youre, "Normal")
elif BMI < 30:
    print(youre, "Overweight")
else:
    print(youre, "Obese")