#!/usr/bin/python3
"""Defines string-to-JSON fx."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
