#!/usr/bin/python3

def no_c(my_string):
    newStr = ""
    for i in my_string:
        if i != "c" and i != "C":
            newStr += i
    return newStr
