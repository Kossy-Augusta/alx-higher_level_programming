#!/usr/bin/python3

'''
    Function
    update_dictionary - Function that replaces or adds
    key/value in a dictionary

    Arguments
    @a-dictionary: a dictionary containinf key value pairs
    @key: name of argument to be added
    @value: value of key
'''


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return (a_dictionary)
