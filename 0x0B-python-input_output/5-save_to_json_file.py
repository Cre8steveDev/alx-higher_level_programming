#!/usr/bin/python3

"""Save a serialized json to a file"""

import json


def save_to_json_file(my_obj, filename):
    """Method that writes serialized JSON to a file"""
    with open(filename, "w", encoding="UTF8") as file:
        serialized = json.dumps(my_obj)
        file.write(serialized)
