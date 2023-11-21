#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed = 0

    for i in range(x):
        try:
            print(f"{my_list[i]}")
            printed += 1
        except:
            printed += 0
    
    return printed
