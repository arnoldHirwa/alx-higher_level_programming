#!/usr/bin/python3

"""Defines a base model class."""
# import json
# import csv
# import turtle


class Base():
    "The base class for shapes"
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
