#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    len_t = len(my_list)

    if idx < 0 or idx >= len_t:
        return my_list

    my_list[idx] = element
    return my_list
