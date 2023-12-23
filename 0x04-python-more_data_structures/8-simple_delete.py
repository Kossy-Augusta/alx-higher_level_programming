#!/usr/bin/python3

'''
    Function
    complex_delete - Function that deletes keys with a
    specific value in a dictionary.

    Arguments
    @a_dictionary: a dictionary of key and value pairs
'''


def simple_delete(a_dictionary, key=""):
    list_of_keys = []
    for keys, value in a_dictionary.items():
        if keys == key:
            list_of_keys.append(key)
    for value in list_of_keys:
        del a_dictionary[value]
    return (a_dictionary)
