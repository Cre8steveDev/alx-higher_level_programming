#!/usr/bin/python3

"""A Module that loads adds and saves"""

import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# Read from the file to see if there's a list

with open("add_item.json", "a+", encoding="UTF8") as file:
    file.seek(0)
    list_in_file = file.read()

    if list_in_file:
        list_in_file = json.loads(list_in_file)

if type(list_in_file) != list:
    list_in_file = []

for x in range(len(sys.argv)):
    if x != 0:
        list_in_file.append(sys.argv[x])

# Write to file
with open("add_item.json", "w", encoding="UTF8") as file:
    file.write(json.dumps(list_in_file))
