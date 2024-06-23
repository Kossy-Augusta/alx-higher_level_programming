#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return (0)
    primary_key = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    values = [
            primary_key[value] for value in roman_string if value
            in primary_key
            ]
    result = 0
    prev = 0
    for value in reversed(values):
        if value < prev:
            result -= value
        else:
            result += value
        prev = value
    return result
