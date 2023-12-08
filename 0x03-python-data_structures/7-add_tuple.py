#!/usr/bin/python3
'''
    Function
    add_tuple - function that adds 2 tuples

    Arguments
    @tuple_a: first tuple
    @tuple_b: second tuple

    Return: A tuple with 2 integers:
    The first element should be the addition
    of the first element of each argument

    The second element should be the addition of the
    second element of each argument
'''


def add_tuple(tuple_a=(), tuple_b=()):
    len_a, len_b = len(tuple_a), len(tuple_b)
    new_tuple = ((tuple_a[0] if len_a >= 1 else 0) +
                 (tuple_b[0] if len_b >= 1 else 0),
                 (tuple_a[1] if len_a >= 2 else 0) +
                 (tuple_b[1] if len_b >= 2 else 0))
    return new_tuple
