#!/usr/bin/python3

'''
    2-safe_print_list_integers.py - Function that prints the first x elements \
            of a list and only integers.
    @my_list: list containing values
    @x: number of elements to access in the list \
            x can be bigger than the length of my_list - \
            if it’s the case, an exception is expected to occur \
            All integers have to be printed on the same line\
            followed by a new line\
            Other type of value in the list must be skipped (in silence).
    Return: The real number of integars printed
'''


def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (ValueError, TypeError):
            pass
    print()
    return num
