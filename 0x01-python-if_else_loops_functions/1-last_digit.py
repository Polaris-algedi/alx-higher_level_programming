#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_dt = abs(number) % 10
if l_dt == 0:
    print(f"Last digit of {number:d} is {l_dt} and is 0")
elif number > 0 and l_dt > 5:
    print(f"Last digit of {number:d} is {l_dt} and is greater than 5")
elif number > 0:
    print(f"Last digit of {number:d} is {l_dt} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {-l_dt} and is less than 6 and not 0")
