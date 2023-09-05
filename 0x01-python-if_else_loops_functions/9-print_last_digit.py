#!/usr/bin/python3

def print_last_digit(number):
    temp = number / 10
    del temp
    digit = int(str(number)[-1])
    print(digit, end="")
    return digit
