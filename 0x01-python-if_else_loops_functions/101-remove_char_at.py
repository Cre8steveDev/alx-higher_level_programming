#!/usr/bin/python3


def remove_char_at(str, n):
    newStr = ""
    for num in range(len(str)):
        if (num == n):
            continue
        newStr += str[num]

    return newStr
