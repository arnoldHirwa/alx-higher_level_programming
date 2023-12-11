#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or type(roman_string) is not str:
        return 0
    else:
        sum = 0
        romArray = [char for char in roman_string[::-1]]
        skip = False
        symbols = {
            "I": {
                "skip": False,
                "value": 1
            },
            "V": {
                "skip": "I",
                "value": 5
            },
            "X": {
                "skip": "I",
                "value": 10
            },
            "L": {
                "skip": "X",
                "value": 50
            },
            "C": {
                "skip": "X",
                "value": 100
            },
            "D": {
                "skip": "C",
                "value": 500
            },
            "M": {
                "skip": "C",
                "value": 1000
            }
        }
        for idx, symbol in enumerate(romArray):
            if skip:
                skip = False
                continue
            else:
                current = symbols[symbol]
                if idx < len(romArray) - 1 and current["skip"] is romArray[idx + 1]:
                    skip = True
                    sum += current["value"] - symbols[current["skip"]]["value"]
                else:
                   sum += current["value"] 
        return sum
