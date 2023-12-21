#!/usr/bin/python3

'''
    Function
    roman_to_int - a function that converts a Roman numeral to an integer.

    Arguments
    @roman_string: String containing roman nummerals

    Return: the value of rman numeral converted to integar.
    0 if the roman_string is not a string or None
'''


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return (0)
    roman_num_value = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    result = 0
    prev = 0
    for alpha in reversed(roman_string):
        for key, value in roman_num_value.items():
            if key == alpha:
                if value < prev:
                    result -= value
                else:
                    result += value
                prev = value
                break
    return (result)
