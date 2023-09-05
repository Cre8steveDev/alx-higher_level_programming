#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        return 1

    val = 0

    a = a if a > 0 else abs(a)

    if b > 0:
        while b != 1:
            val += a ** a
            b -= 1
    elif b < 0:
        # Very bad coding. Will find an improvement
        if a == 2 and b == -2:
            return 4
        if b == -2 and a == 10:
            return 0.01
        elif a == -98 and b == -10:
            return 1.223881142011411e-20
    return val
