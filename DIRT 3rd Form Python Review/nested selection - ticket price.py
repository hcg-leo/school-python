night = input("Is it night? (Y or N) ")
distance = int(input("How far will you travel in miles? "))
if night == "Y":
    if distance < 5:
        price = 10
        difference = 3
    elif distance <= 10:
        price = 20
        difference = 2
    else:
        price = 30
        difference = 5
else:
    if distance < 5:
        price = 7
    elif distance <= 10:
        price = 18
    else:
        price = 25
print(f"The fare is £{price}")
if night == "Y":
    print(f"It would have been £{difference} cheaper during the day")
