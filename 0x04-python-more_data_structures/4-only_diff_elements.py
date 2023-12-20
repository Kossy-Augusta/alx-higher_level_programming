#!/usr/bin/python3

'''
    Function
    only_diff_elements - Function that returns a set of all
    elements present in only one set

    Arguments
    @set_1 and set_2: unique sets
'''


def only_diff_elements(set_1, set_2):
    values = set_1 ^ set_2
    return (values)
