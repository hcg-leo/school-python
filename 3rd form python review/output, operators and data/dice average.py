# Mark: Complete — two valid random dice values are generated and their average is correctly rounded to 1 decimal place.
# Improvement: Use descriptive labels when printing the dice values and average.
import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print(dice1)
print(dice2)
print(round((dice1 + dice2) / 2, 1))