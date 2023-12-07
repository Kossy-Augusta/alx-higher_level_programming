#!/usr/bin/python3

'''
    Function
    no_c - function that removes all characters c and C from a string

    Arguments
    @my_string: string to be worked on

    Return: New string
'''


def no_c(my_string):
    new_string = ""
    for elem in my_string:
        if elem != 'c' and elem != 'C':
            new_string += elem

    return (new_string)
