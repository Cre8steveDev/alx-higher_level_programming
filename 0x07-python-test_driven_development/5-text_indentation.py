#!/usr/bin/python3

"""Funny replace certain characters with two lines"""


def text_indentation(text):
    """Text indentation funny"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text_array = text.split()
    characters = {"?", ".", ":"}

    for word in text_array:
        print(word, end="")

        if not (set(word) & characters):
            if not (word == text_array[-1]):
                print(" ", end="")

        if set(word) & characters:
            print("\n")
