#!usr/bin/python3

def square_matrix_simple(matrix=[]):
    newList = []
    for mem in matrix:
        newList.append((list(map(lambda x: x**2, mem))))

    return newList
