# Mark: Complete — math is imported, the area formula is correct, and the result is rounded to 2 decimal places.
# Improvement: Label the output so the user knows the number is the area.
import math
radius = float(input("What is the radius of you circle? "))
print(round(math.pi * radius ** 2, 2))