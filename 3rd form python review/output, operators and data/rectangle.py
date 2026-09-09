# Mark: Complete — float inputs, area and perimeter calculations, and 1-decimal rounding are all correct.
# Improvement: Add labels such as "Area:" and "Perimeter:" to make the output clearer.
length = float(input("Length: "))
width = float(input("Width: "))
print(round(length * width, 1))
print(round(2 * (length + width), 1))