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
        result = a / b
    except Exception:
        result = None
    finally:
        print("Insisde result: {}".format(result))
    return result
