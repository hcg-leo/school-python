# Mark: Complete — correctly identifies odd/even and positive/negative/zero using selection.
# Improvement: Good clear use of if/elif/else; consider adding punctuation to the user-facing messages.
number = int(input("Enter a number "))
if number % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")
if number > 0:
    print("This number is positive")
elif number < 0:
    print("This number is negative")
else:
    print("This number is zero")