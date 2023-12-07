#!/usr/bin/python3

'''
    Function
    element_at - Function that retrieves an element from a list
    Arguments
    @my_list: list of elements
    @idx: position od the element

    Return: None if ix is negative or None if idx is
    out of range or element in idx
'''


def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0:
        return (None)
    elif idx > length - 1:
        return (None)
    else:
        return (my_list[idx])
