#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


test = number / 10
del test

if number < 0:
    num = int(str(number)[-1])
    print(f"Last digit of {number} is -{num} and is less than 6 and not 0")
else:
    num = str(number)[-1]
    digit = int(num)
    if digit > 5:
        print(f"Last digit of {number} is {digit} and is greater than 5")
    elif digit == 0:
        print(f"Last digit of {number} is {digit} and is 0")
    else:
        print(f"Last digit of {number} is {num} and is less than 6 and not 0")
