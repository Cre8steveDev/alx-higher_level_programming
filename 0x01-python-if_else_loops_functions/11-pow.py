#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        return 1

    val = None

    a = a if a > 0 else abs(a)

    if b > 0:
        while b != 1:
            val = a ** a
            b -= 1
    elif b < 0:
        while b != -1:
            val = a ** a
            b += 1
    return val
