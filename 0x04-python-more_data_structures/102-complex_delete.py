#!/usr/bin/python3

'''
    Function
    complex_delete - Function that deletes keys with a
    specific value in a dictionary.

    Arguments
    @a_dictionary: a dictionary of key and value pairs
'''


def complex_delete(a_dictionary, value):
    list_of_keys = []
    for key, values in a_dictionary.items():
        if values == value:
            list_of_keys.append(key)
    for keys in list_of_keys:
        del a_dictionary[keys]
    return a_dictionary
