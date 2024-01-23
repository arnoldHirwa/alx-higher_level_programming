#!/usr/bin/python3
"""A module for reading input commands from stdin"""


def printInfo(size, codes):
    """A function for printing information to stdout"""
    print(f"File size: {size}")
    for key in sorted(codes):
        print(f"{key}: {codes[key]}")


if __name__ == "__main__":
    import sys

    size = 0
    codes = {}
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    i = 0
    try:
        for data in sys.stdin:
            if i % 10 == 0 and i != 0:
                printInfo(size, codes)
            i += 1
            data = input()
            splitted = data.split()
            try:
                size += int(splitted[-1])
            except Exception:
                pass
            try:
                code = int(splitted[-2])
                if code in valid_codes:
                    codes[code] = codes.get(code, 0) + 1
            except Exception:
                pass

        printInfo(size, codes)
    except KeyboardInterrupt:
        printInfo(size, codes)
        raise
