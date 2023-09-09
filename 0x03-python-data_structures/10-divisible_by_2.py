#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return []

    check_list = []

    for item in my_list:
        if item % 2 == 0:
            check_list.append(True)
        else:
            check_list.append(False)

    return check_list
