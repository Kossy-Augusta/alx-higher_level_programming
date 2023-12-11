#!/usr/bin/python3

'''
    Function
    delete_at - a function that deletes the item at a
    specific position in a list

    Arguments
    @my_list: list of integars
    @idx: position of the element in the list

    Return: returns original list if idx is negative or out
    of range or modified list in which item at id has been removed
'''


def delete_at(my_list=[], idx=0):
    if my_list:
        if idx < 0 or idx > (len(my_list) - 1):
            return (my_list)
        else:
            del my_list[idx]
        return (my_list)
