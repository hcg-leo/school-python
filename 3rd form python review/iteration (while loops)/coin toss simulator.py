import random
heads = 0
tails = 0
count = 0

while count < 200:
    flip = random.randint(1, 2)
    if flip == 1:
        heads = heads + 1
    else:
        tails = tails + 1
    count = count + 1
print(f"{tails} tails,  {heads} heads")
print(f"{tails / 2}% for tails, {heads / 2}% for heads.")