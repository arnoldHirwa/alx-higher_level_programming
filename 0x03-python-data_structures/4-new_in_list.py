#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new = my_list.copy()  # Create a copy of my_list to start with

    if (idx < 0 or idx > (len(my_list) - 1)):
        return new
    else:
        new[idx] = element
        return new
