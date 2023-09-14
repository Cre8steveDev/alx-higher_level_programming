#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    final_dict = dict()
    for key, val in a_dictionary.items():
        if val == value:
            print(key, val)
            continue
        final_dict[key] = value

    a_dictionary = final_dict
    return a_dictionary
