#!/usr/bin/python3

def multiple_returns(sentence):
    try:
        return ((len(sentence), sentence[0]))
    except:
        return((0, None))
