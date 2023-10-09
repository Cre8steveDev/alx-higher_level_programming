#!/usr/bin/python3

"""Function that looks up the methods of an object"""


def lookup(obj):
    """Checks what methods are available in an object
    Arguments: obj - Object to be checked
    Return: A list
    """
    return dir(obj)
