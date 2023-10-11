#!/usr/bin/python3

"""Read from a JSON file"""

import json


def load_from_json_file(filename):
    "Loads from a json file"
    with open(filename, "r", encoding="UTF8") as JSON_file:
        new_str = JSON_file.read()

        return json.loads(new_str)
