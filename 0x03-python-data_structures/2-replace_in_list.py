#!/usr/bin/python3

'''
    Function
    replace_in_list - function that replaces an
    element of a list at a specific position

    Arguments
    @my_list: list of elements
    @idx: position of the element
    @element: element to be added

    Return: original list if idx is negative or
    original list if idx is out of range or
    the new modified list if idx is out of range or less than 0
'''


def replace_in_list(my_list, idx, element):
    length = len(my_list)

    if idx < 0:
        return (my_list)
    elif idx > length - 1:
        return (my_list)
    my_list[idx] = element
    return (my_list)
