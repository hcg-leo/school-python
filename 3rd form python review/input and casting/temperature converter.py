# Mark: Complete — correct float input, conversion formula, f-string, and rounding to 1 decimal place.
# Improvement: The result is already rounded; remove "rounded to 1 decimal place" from the displayed sentence.
cel = float(input("What is the temp in cel? "))
fahren = round((cel * 9 / 5) + 32, 1)
print(f"{cel} degrees C is {fahren} degrees F rounded to 1 decimal place.")