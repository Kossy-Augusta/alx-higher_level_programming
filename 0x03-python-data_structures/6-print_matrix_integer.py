#!/usr/bin/python3

'''
    Function
    print_matrix_integer - function that prints a matrix of integers

    Arguments
    @matrix: matrix to be printed

'''


def print_matrix_integer(matrix=[[]]):
    if matrix:
        length_row = len(matrix)
        length_col = len(matrix[0])
        # loop through row and column
        for i in range(length_row):
            for j in range(length_col):
                if j < length_col - 1:
                    print("{:d}".format(matrix[i][j]), end=" ")
                else:
                    print("{:d}".format(matrix[i][j]), end="")
            print()
