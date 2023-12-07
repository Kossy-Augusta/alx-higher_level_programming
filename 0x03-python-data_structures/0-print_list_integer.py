#!/usr/bin/python3

'''
    Function print_list_integer
    function that prints all integers of a list

    Arguments:
    @my_list: list contaioning integers
'''


def print_list_integer(my_list=[]):
    for element in my_list:
        print("{:d}".format(element))
