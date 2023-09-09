#!/usr/bin/python3

def element_at(my_list, idx):

    len_t = len(my_list)

    if idx < 0 or idx >= len_t:
        return None

    return my_list[idx]
