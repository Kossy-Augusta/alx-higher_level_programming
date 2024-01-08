#!/usr/bin/python3
import sys

'''
safe_function - function that executes a function safely.
@fct: pointer to a function
@args: Variadic number odf arguments
Return: result of the function fct otherwise return None if an exception \
        occurs during the function and prints in stderr the error\
        precede by Exception:
'''


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return(result)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return (None)
