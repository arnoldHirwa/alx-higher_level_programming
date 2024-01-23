#!/usr/bin/python3
"""A module for reading input commands from stdin"""
import sys


totalSize = 0
codes = {}


def printInfo():
    """A function for printing information to stdout"""
    print("Filse size: ", totalSize)
    for key in sorted(codes.keys()):
        print(f"{key}: {codes[key]}")


if __name__ == "__main__":
    i = 1
    while True:
        try:
            data = input()
            splitted = data.split()
            code = int(splitted[-2])
            size = splitted[-1]
            totalSize += int(size)
            codes[code] = codes.get(code, 0) + 1
            if i % 10 == 0:
                printInfo()
        except KeyboardInterrupt:
            printInfo()
            break
        i += 1
