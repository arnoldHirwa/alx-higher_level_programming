#!/usr/bin/python3
"""
This is text indentation module.
This module supplies one function, text_indentation().
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after these characters: . ? :
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    newline = True
    for c in text:
        if not (newline and c == ' '):
            print(c, end='')
            newline = False
            if c in '.?:':
                print('\n')
                newline = True
