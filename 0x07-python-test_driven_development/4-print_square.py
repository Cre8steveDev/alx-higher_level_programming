#!/usr/bin/python3


"""Printing a Square"""


def print_square(size):
    """A function that prints a square"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    i = 0
    while i < size:
        for _ in range(size):
            print("#", end="")
        print()
        i += 1
