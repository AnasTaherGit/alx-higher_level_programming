#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_value = 0
    for i in reversed(roman_string):
        if roman_dict[i] >= prev_value:
            total += roman_dict[i]
        else:
            total -= roman_dict[i]
        prev_value = roman_dict[i]
    return total
