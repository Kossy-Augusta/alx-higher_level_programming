#!/usr/bin/python3

'''
safe_print_division - Function that divides 2 integers and \
        prints the result.
@a: first integar
@b: second integar
Return: value of the division, otherwise: None
'''


def safe_print_division(a, b):
    try:
        value = a / b
    except ZeroDivisionError:
        value = None
    finally:
        print("Inside result: {}".format(value))
        return value
