#!/usr/bin/python3

"""Converts attributes of a class to dictionary"""


def class_to_json(obj):
    """Method that converts object attributes to dictionary"""
    object_attr = obj.__dict__
    serialized = {}

    for key, value in object_attr.items():
        serialized[key] = value

    return serialized
