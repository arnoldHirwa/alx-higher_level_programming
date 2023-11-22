#!/usr/bin/python3
"""Define square with position coordinates."""


class Square:
    """Class Square is created."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes with a size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """This methof is for returning size value."""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set a size value."""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
            """Verify that size is not negative or 0"""
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size**2

    def my_print(self):
        """Prints square with # in stdout."""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(0, self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
                """print the square"""
    @property
    def position(self):
        """Keep position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set value of position."""
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int\
           or type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
