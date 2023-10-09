#!/usr/bin/python3

"""Check if an object is a subclass or sub class of another"""


def inherits_from(obj, a_class):
    """Check if an object is  subclass

    Args:
            obj (Any): Object
            a_class (Any): Class type
    """
    return type(obj) is a_class
