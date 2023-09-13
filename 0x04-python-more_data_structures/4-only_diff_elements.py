#!/usr/bin/pthon3

def only_diff_elements(set_1, set_2):
    # setF = set()

    # for elem in set_1:
    #     if elem not in set_2:
    #         setF.add(elem)

    # for elet in set_2:
    #     if elet not in set_1:
    #         setF.add(elet)
    setF = set_1 ^ set_2

    return setF
