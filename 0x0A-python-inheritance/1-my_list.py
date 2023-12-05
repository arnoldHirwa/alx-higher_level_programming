#!/usr/bin/python3
"""A module of MyList class"""

class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints a list in a sorted way"""
        print(sorted(self))
