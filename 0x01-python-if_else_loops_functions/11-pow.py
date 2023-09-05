#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        return 1
    if b > 0:
        while b != 0:
            a ** a
            b -= 1
    elif b < 0:
        while b != 0:
            a ** a
            b += 1
    return a
