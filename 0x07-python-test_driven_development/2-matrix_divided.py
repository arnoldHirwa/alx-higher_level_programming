#!/usr/bin/python3
"""
This is the matrix divided module.
function that divides all elements of a matrix, matrix_divided().
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix with all elements divided by div.
    """
    men1 = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(men1)

    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(men1)
        for col in matrix[0]:
            if type(col) is not int and type(col) is not float:
                raise TypeError(men1)

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new = [row[:] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            new[row][col] = round(matrix[row][col] / div, 2)

    return new
