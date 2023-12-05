#!/usr/bin/python3
"""A module for task 4"""

def inherits_from(obj, a_class):
    """Returns true if instance of class that
        inherited a_class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
