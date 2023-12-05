#!/usr/bin/python3
"""Module to Task Advanced 100"""


class MyInt(int):
    """MyInt class."""
    pass

    def __eq__(self, other):
        """Verify if two MyInts are equal."""
        return int(self) != int(other)

    def __ne__(self, other):
        """Verify if two MyInts are not equal."""
        return int(self) == int(other)
