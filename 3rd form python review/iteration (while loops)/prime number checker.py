number = int(input("enter a positive integer: "))
if number < 2:
    print(f"{number} is not prime")
else:
    factor = 2
    is_prime = True
 while factor < number:
    if number % factor == 0:
        is_prime = False
    factor += 1
    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")