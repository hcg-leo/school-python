score = 1
total = 0
entered = 0
highest = 0
lowest = score
while score != -1:
    score = int(input("Enter your exam score. "))
    total = total + score
    entered = entered + 1
    if score > highest:
        highest = score
    elif score < lowest:
        lowest = score
average = round(total / entered)
print(f"Scores entered {entered}")
print(f"total {total}")
print(f"average {average}")
print(f"highest score {highest}")
print(f"lowest score {lowest}")