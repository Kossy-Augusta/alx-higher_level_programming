#!/usr/bin/python3

'''
    Function
    uniq_add - function that adds all unique integers in a
    list (only once for each integer)

    Arguments
    @my_list: list of elements

'''


def uniq_add(my_list=[]):
    new = set(my_list)
    result = 0
    for i in new:
        result += i
    return (result)
