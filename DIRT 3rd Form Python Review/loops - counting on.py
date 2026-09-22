start = int(input("Enter the starting value "))
stop = int(input("Enter the last value "))
step = int(input("Enter the step amount "))
if start <= stop:
    while start <= stop:
        print(start)
        start = start + step
else:
    while start >= stop:
        print(start)
        start = start - step