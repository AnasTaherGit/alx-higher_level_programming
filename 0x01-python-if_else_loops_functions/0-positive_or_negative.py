#!/usr/bin/python3
import random
TheRandomNumber = random.randint(-10, 10)
if TheRandomNumber > 0:
    print(f"{TheRandomNumber:d} is positive")
elif TheRandomNumber == 0:
    print(f"{TheRandomNumber:d} is zero")
else:
    print(f"{TheRandomNumber:d} is negative")
