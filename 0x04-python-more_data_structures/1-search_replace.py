#!/usr/bin/python3

'''
    Function
    search_replace - Function that replaces all occurrences
    of an element by another in a new list

    Arguments
    @my_list: list of elements
    @search: element to be replaced in the list
    @replace: the new element

    Return: the new list
'''


def search_replace(my_list, search, replace):
    if my_list:
        new = [replace if x == search else x for x in my_list]

        return (new)
    return (my_list)
