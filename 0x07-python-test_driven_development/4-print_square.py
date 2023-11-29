#!/usr/bin/python3
"""
This is print square module.
"""


def print_square(size):
    """
    Print a square using character #
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    print(('#' * size + '\n') * size, end='')
