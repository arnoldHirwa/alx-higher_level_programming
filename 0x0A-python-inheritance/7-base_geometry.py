#!/usr/bin/python3
"""Module for task 7"""


class BaseGeometry():
    """A class to task7"""
    def area(self):
        """Use an Exception for area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """To validate value and raises exceptions."""
        if not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
