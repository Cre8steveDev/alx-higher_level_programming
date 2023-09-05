#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        return 1
    if b > 0:
        while a != 0:
            a ** a
            a -= 1
    if b < 0:
        while a != 0:
            a ** a
            a += 1
