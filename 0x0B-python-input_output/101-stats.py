#!/usr/bin/python3
"""A module for reading input commands from stdin"""
import sys


totalSize = 0
codes = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']


def printInfo():
    """A function for printing information to stdout"""
    print("File size: ", totalSize)
    for key in sorted(codes.keys()):
        print(f"{key}: {codes[key]}")


if __name__ == "__main__":
    i = 1
    while True:
        try:
            data = input()
            splitted = data.split()
            try:
                size = splitted[-1]
                totalSize += int(size)
            except Exception:
                pass
            try:
                code = int(splitted[-2])
                if str(code) in valid_codes:
                    codes[code] = codes.get(code, 0) + 1
            except Exception:
                pass

            if i % 10 == 0:
                printInfo()
        except KeyboardInterrupt:
            printInfo()
            raise
        i += 1
