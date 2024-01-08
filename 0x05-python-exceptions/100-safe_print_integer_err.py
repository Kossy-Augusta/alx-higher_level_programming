#!/usr/bin/python3
import sys

'''
safe_print_integer_err - function that prints an integer.
@value:  can be any type (integer, string, etc.)
Return: Returns True if value has been correctly printed\
        (it means the value is an integer) otherwis return False\
        and prints in stderr the error precede by Exception:
'''


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        return True
