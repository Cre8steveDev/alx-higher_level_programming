#!/usr/bin/python3

"""A Module that divites all integers within a matrix"""


def matrix_divided(matrix, div):
    """Matrix dividing function"""

    same_length = all(len(row) == len(matrix[0]) for row in matrix)
    all_numbers = all(type(item) in [int, float]
                      for row in matrix for item in row)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all_numbers:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not same_length:
        raise TypeError("Each row of the matrix must have the same size")

    final_matrix = []
    for _array in matrix:
        final_matrix.append(
            list(map(lambda x:
                     round(x / div, 2),
                     _array)))

    return final_matrix
