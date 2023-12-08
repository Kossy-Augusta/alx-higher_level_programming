#!/usr/bin/python3

'''
    Function
    max_integer - function that finds the biggest integer of a list

    Arguments
    @my_list: list of integars

    Return: None if list is empty or biggest integar if list is not empty

'''


def max_integer(my_list=[]):
    # find the length of the list
    length = len(my_list)
    # check if length is 0, if yes, return None
    if length == 0:
        return
    # create a var highest that holds the highest value and assign it [0]
    highest = my_list[0]
    # Loop through the list at a range of 0 - length - 1
    for i in range(length - 1):
        # check if i+1 is greater than highest, if yes, reassign
        if my_list[i + 1] > highest:
            highest = my_list[i + 1]
    return (highest)
