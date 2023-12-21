#!/usr/bin/python3

'''
    Function
    best_score -  function that returns a key with the biggest integer value

    Arguments
    @a-dictionary: a dictionary containinf key value pairs

    Return: a key with the biggest integer value
'''


def best_score(a_dictionary):
    if a_dictionary:
        highest = 0
        for key, value in a_dictionary.items():
            if value > highest:
                key_value = key
                highest = value
        return (key_value)
    else:
        return
