#!/usr/bin/python3

"""Create a readfile module"""


def read_file(filename=""):
    """Opens and reads from a file"""
    with open(filename, "r", encoding="UTF8") as file:
        content = file.read()

    print(content, end="")
