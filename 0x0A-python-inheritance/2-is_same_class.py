#!/usr/bin/python3
"""Module to Task 2."""


def is_same_class(obj, a_class):
    """Returns true or false, if object is an instance of class."""
    if type(obj) is a_class:
        return True
    else:
        return False
