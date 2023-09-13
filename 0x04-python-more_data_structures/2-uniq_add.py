#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniqu = []

    for itr in my_list:
        if itr in uniqu:
            continue
        uniqu.append(itr)

    return sum(uniqu)
