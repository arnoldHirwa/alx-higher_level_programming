#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        i = str[i]
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
        print('{}'.format(i), end='')
    print()
