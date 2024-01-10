#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    num = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    prev_val = 0

    for char in reversed(roman_string):
        value = num[char]
        total += value if value >= prev_val else -value
        prev_val = value
    return total
