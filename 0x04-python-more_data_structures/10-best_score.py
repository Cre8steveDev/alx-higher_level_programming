#!/usr/bin/python3

def best_score(a_dictionary):

    if not a_dictionary:
        return None

    temp, temp2 = 0, ""

    for key, value in a_dictionary.items():

        if value > temp:
            temp = value
            temp2 = key

    return temp2
