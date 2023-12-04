#!/usr/bin/python3
"""A function that checks if an object is of a certain class"""


def is_same_class(obj, a_class):
    """Returns True if obj and a_class are same"""
    return type(obj) is a_class
