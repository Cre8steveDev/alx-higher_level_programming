#!/usr/bin/python3

"""Check if an object is a class or sub class of another"""


def is_kind_of_class(obj, a_class):
    """Check if an object is of same class

    Args:
            obj (Any): Object
            a_class (Any): Class type
    """
    return (isinstance(obj, a_class))
