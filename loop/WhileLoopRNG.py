import random

n = []

while True:
    x = random.randint(1,100)
    
    if (x % 5==0):
        print(x)
        break

    elif (x % 3==0):
        print(x)
        print("Skipping")
        continue

print(x)