#!/usr/bin/python3
"""
Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    matrix division function
    Args:
        matrix (list of lists of integers or floats)
        div (float or int)
    Returns:
        a new matrix
    Raises:
        TypeError if :
            matrix is not a list of lists
            matrix rows are not of the same size
            div is not a number
        ZeroDivisionError if div is equal to zero
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(error_msg)
        for i in row:
            if not isinstance(i, int):
                raise TypeError(error_msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    return ([[round(i / div, 2) for i in row] for row in matrix])
