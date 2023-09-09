#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix[0] == []:
        print()
    for outer in matrix:
        for idx, elem in enumerate(outer):
            if idx == len(outer) - 1:
                print("{:d}".format(elem))
            else:
                print("{:d} ".format(elem), end="")
