#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(number, "is postitive")
if number == 0:
    print(number, "is zero")
if number < 0:
    print(number, "is negative")
