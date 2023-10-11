#!/usr/bin/python3

"""Write content to a file Module"""


def write_file(filename="", text=""):
    """This method writes to a file and overwrites"""
    with open(filename, "w", encoding="UTF8") as file:
        char_written = file.write(text)

    return char_written
