#!/usr/bin/python3

"""A module that returns a JSON"""
import json


def to_json_string(my_obj):
    """This function returns a JSON from an object"""
    return json.dumps(my_obj)
