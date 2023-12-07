#!/usr/bin/python3

'''
    Function
    new_in_list - function that replaces an element in a
    list at a specific position without modifying the original list

    Arguments
    @my_list: list of elements
    @idx: position of the element
    @elemet: element to be added

    Return: A copy of original list if idx is negative or
    A copy of original list  if idx is out of range or
    A copy of original list with element at position idx modified to element
'''


def new_in_list(my_list, idx, element):
    if my_list:
        new_list = my_list[:]
        if idx < 0:
            return (new_list)
        elif idx > (len(my_list) - 1):
            return (new_list)
        new_list[idx] = element
        return (new_list)
