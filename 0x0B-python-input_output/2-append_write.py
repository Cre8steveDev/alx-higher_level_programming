#!/usr/bin/python3

"""A Module with function that appends to a file"""


def append_write(filename="", text=""):
    """Append to a file"""
    with open(filename, "a", encoding="UTF8") as file:
        char_written = file.write(text)

    return char_written
