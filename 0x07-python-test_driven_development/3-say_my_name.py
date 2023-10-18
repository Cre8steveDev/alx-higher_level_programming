#!/usr/bin/python3

""""Say My Name Module - Task 3"""


def say_my_name(first_name, last_name=""):
    """Say my name module"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if len(last_name) < 1:
        print(f"My name is {first_name}")
        return

    print(f"My name is {first_name} {last_name}")