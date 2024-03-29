#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_map = {'I': 1, 'V': 5,
                 'X': 10, 'L': 50,
                 'C': 100, 'D': 500,
                 'M': 1000}
    result = 0
    if (type(roman_string) != str) or roman_string is None:
        return 0
    for i in range(len(roman_string)):
        curr = roman_map[roman_string[i]]
        if i+1 < len(roman_string) and roman_map[roman_string[i+1]] > curr:
            result -= curr
        else:
            result += curr
    return result
