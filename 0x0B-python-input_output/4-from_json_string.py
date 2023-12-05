#!/usr/bin/python3

"""Converts from JSON String back to object
This is called Deserialization
"""

import json


def from_json_string(my_str):
    """From json string to python object"""
    return json.loads(my_str)
