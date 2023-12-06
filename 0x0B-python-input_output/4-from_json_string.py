#!/usr/bin/python3
# 6-from_json_string.py
"""Defines JSON-to-object fx."""
import json


def from_json_string(my_str):
    """Return the Python object representation of JSON string."""
    return json.loads(my_str)
