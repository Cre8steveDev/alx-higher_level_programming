#!/usr/bin/python3

"""A Module that contains a method
that adds two integers"""


def add_integer(a, b=98):
    """Adds two integers with the second
    argument being optional"""

    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")

    if (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    a = input("Enter first: ")
    b = input("Enter second: ")

    result = add_integer(a, b)

    print(result)
