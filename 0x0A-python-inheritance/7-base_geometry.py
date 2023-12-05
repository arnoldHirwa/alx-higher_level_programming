#!/usr/bin/python3
"""Module for task 7"""

class BaseGeometry():
    """a BaseGeometry class"""
    
    def area(self):
        """retuns an area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise Exception(f'{name} must be an integer')
        elif value <= 0:
            raise Exception(f'{name} must be greater than 0')
