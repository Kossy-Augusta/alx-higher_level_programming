#!/usr/bin/python3

'''
    Function
    square_matrix_simple - Function that computes the square
    value of all integers of a matrix.

    Arguments
    @matrix: a 2 dimmensional array

    Return: a new matrix same size as matrix where each value is a square of
    the input
'''


def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = [[element ** 2 for element in row] for row in matrix]
        return new_matrix
