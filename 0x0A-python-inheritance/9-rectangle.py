#!/usr/bin/python3
"""Module to Task 9"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """To raise an exception."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """To validate value."""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __repr__(self):
        """To print the width and height of the rectangle."""
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """To return the area of the rectangle."""
        return self.__width * self.__height
