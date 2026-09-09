# Mark: Complete — correct float inputs, BMI formula, and rounding to 1 decimal place.
# Improvement: Label the result, e.g. print(f"BMI: {round(bmi, 1)}").
weight = float(input("What is your weight in kg? "))
height = float(input("What is your height in meters? "))
bmi = weight / (height * height)
print(round(bmi, 1))