#!/usr/bin/python3

'''
    Function
    print_sorted_dictionary - function that prints a
    dictionary by ordered keys.

    Arguments
    @a_dictionary: a dictionary
'''


def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary)
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
