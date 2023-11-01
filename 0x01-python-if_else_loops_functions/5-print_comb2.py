#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print('0{}'.format(i), end=", ")
    else:
        if i == 99:
            print(i)
        else:
            print(i, end=", ")
