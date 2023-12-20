#!/usr/bin/python3

'''
    Function
    multiply_by_2 - function that returns a new dictionary
    with all values multiplied by 2

    Arguments
    @a-dictionary: a dictionary containinf key value pairs

    Return: a new dictionary with all values multiplied by 2
'''


def multiply_by_2(a_dictionary):
    new = dict()

    for k, v in a_dictionary.items():
        new[k] = v * 2
    return (new)
