#!/usr/bin/python3
import random
TheRandomNumber = random.randint(-10000, 10000)
ComputedDigit = abs(TheRandomNumber) % 10 * (-1 if TheRandomNumber < 0 else 1)
print(
    f"Last digit of {TheRandomNumber:d} is {ComputedDigit:d} and is ", end="")
if ComputedDigit > 5:
    print("greater than 5")
elif ComputedDigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
