#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    divisors = list(map(lambda x: x[-1], my_list))
    topper = list(map(lambda x: x[0] * x[-1], my_list))

    return sum(topper)/sum(divisors)
