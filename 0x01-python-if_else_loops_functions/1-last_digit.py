#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ComputedDigit = abs(number) % 10 * (-1 if number < 0 else 1)
print(
    f"Last digit of {number :d} is {ComputedDigit:d} and is ", end="")
if ComputedDigit > 5:
    print("greater than 5")
elif ComputedDigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
