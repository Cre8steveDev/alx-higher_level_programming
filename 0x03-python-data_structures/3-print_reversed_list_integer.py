#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    if not my_list:
        return

    my_list.reverse()
    rev_list = my_list

    for item in rev_list:
        print("{}".format(item))
