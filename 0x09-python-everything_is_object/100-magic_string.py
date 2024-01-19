#!/usr/bin/python3
def magic_string():
    magic_string.static = getattr(magic_string, 'static', -1) + 1
    return "BestSchool, " * magic_string.static + "BestSchool"
