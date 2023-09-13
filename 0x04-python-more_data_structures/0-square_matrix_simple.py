#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    finalList = []

    for i in range(len(matrix)):
        finalList += [list(map(lambda x: x ** 2, matrix[i]))]

    return finalList
