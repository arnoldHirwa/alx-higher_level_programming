#!/usr/bin/python3


"""The square module"""


class Square:
    """The summary line for a class docstring should fit on one line."""

    def __init__(self, size=0):
        """The summary line for a class docstring should fit on one line."""
        self.size = size

    def area(self):
        """The summary line for a class docstring should fit on one line."""
        return (self._size * self._size)

    @property
    def size(self):
        """The summary line for a class docstring should fit on one line."""
        return self._size

    @size.setter
    def size(self, value):
        """The summary line for a class docstring should fit on one line."""
        if type(value) == int:
            if value >= 0:
                self._size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le___(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()