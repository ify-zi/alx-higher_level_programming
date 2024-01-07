#!/usr/bin/python3
"""
    matrix divider
"""


def matrix_divided(matrix, div):
    """divide a matrix by div"""
    new_list = []
    r_len = len(matrix[0])
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")
    for item in matrix:
        if len(item) != r_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
