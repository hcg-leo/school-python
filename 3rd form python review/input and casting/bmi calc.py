weight = float(input("What is your weight in kg? "))
height = float(input("What is your height in meters? "))
bmi = weight / (height * height)
print(round(bmi, 1))