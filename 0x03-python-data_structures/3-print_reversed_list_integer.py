#!/usr/bin/python3

'''
    Function
    print_reversed_list_integer - Function that prints all
    integers of a list, in reverse order.

    Arguments
    @my_list: list of elements

'''


def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return
    length = len(my_list)
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
