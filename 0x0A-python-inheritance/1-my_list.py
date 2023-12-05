#!/usr/bin/python3
"""Module Task1 - class MyList that inherits from list."""


class MyList(list):
    """Module to MyList."""

    def print_sorted(self):
        """Print the list and sort it in ascending order."""
        print(sorted(self))
