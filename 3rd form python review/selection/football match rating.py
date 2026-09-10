goals = int(input("Enter the number of goals scored in a football match. "))
if goals == 0:
    print("The game was a bore")
elif goals <= 2:
    print("Not the most exciting match")
elif goals <= 5:
    print("A great match!")
else:
    print("Unmissable!")