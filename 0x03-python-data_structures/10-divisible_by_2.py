#!/usr/bin/python3

'''
    Function
    divisible_by_2 - function that finds all multiples of 2 in a list

    Arguments
    @my_list: list of integars

    Return:  a new list with True or False, depending on
    whether the integer at the same position in the
    original list is a multiple of 2
'''


def divisible_by_2(my_list=[]):
    new_list = []
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
        i += 1
    return new_list
