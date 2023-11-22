#!/usr/bin/python3
"""Define a method called area to find the square."""


class Square:
    """Class Square is created"""

    def __init__(self, size=0):
        """Initializes the class with a size"""

        if type(size) is not int:
            raise TypeError('size must be an integer')
            """Verify that size is not an integer"""
        if size < 0:
            raise ValueError('size must be >= 0')
            """Verify that size is not negative or 0"""
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size**2
