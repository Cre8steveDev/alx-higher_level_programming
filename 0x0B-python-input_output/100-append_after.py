#!/usr/bin/python3

"""Append to a file if it contains a certain string"""


def append_after(filename="", search_string="", new_string=""):
    """Appends after it finds a string match"""

    # Open the file and read to a variable
    with open(filename, "r", encoding="UTF8") as file:
        lines_list = file.readlines()

    # Append to the file with write and modify
    with open(filename, "w", encoding="UTF8") as file:
        for line in lines_list:
            file.write(line)

            if search_string in line:
                file.write(new_string)
