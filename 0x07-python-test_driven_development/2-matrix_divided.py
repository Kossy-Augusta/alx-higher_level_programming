#!/usr/bin/python3

"""2-matrix_divided.py module

contains a function matrix_divided(..),that divides all elements in a matrix
"""


def matrix_divided(matrix, div):
    """Divides all element of a matrix

    Args:
        matrix (list of lists): matrix that contains a list of list of\
                integars/floats
        div (int or float): a number that divides the elements in the matrix
    Returns: a new matrix
    Raises an error if matrix is not a list of lists or if div is 0 or a\
            non-number value or matrix rows are not of same size
"""
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
