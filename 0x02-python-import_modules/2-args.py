#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
        if len(argv) == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(len(argv)))
        for n in range(1, len(argv)):
            print("{}: {}".format(n, argv[n]))
