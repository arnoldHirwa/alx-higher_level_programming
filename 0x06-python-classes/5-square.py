#!/usr/bin/python3
"""Define a getter and setter for a square's size."""


class Square:
    """Class Square is created"""

    def __init__(self, size=0):
        """Initializes with a size"""
        self.size = size

    @property
    def size(self):
        """Set and Return size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set a size value"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
            """Verify that size is not negative or 0"""
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size**2

    def my_print(self):
        """print the square with # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
