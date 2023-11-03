#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    all = argv[1:]
    sum = 0
    for i in all:
        sum += int(i)
    print("{}".format(sum))
