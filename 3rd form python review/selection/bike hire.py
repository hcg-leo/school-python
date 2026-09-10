age = int(input("how old are you? "))
hours = int(input("how many hours do you need to ride for? "))
if age < 16:
    print("sorry you must be 16 or over to hire a bike")
else:
    if hours <= 2:
    print("the cost is £8 per hour")
 else:
    print("the cost is £6 per hour")
