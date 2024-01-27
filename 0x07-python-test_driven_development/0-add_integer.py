#!usr/bin/python3
"""0-add_integer Module

This module defines a function add_integer
add_integer return the addition of two integars
"""


def add_integer(a, b=98):
    """add_integer function returns integer value of a + b
    Float arguments are type casted to int before addition.
    Raises TypeError if either a or b is non-integar and non-float
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if type(a) != int:
        a = int(a)
    if type(b) != int:
        b = int(b)
    return a + b
