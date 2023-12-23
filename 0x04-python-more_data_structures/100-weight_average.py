#!/usr/bin/python3

'''
    Function
    weight_average - unction that returns the weighted
    average of all integers tuple (<score>, <weight>)

    Arguments
    @my_list: list

    Return:0 if the list is empty or weighed averayge if the list is not empty
'''


def weight_average(my_list=[]):
    if my_list:
        length = len(my_list)
        total = 0
        div = 0
        for value in my_list:
            mult = value[0] * value[1]
            div += value[1]
            total += mult
        result = total / div
        return (result)
    else:
        return (0)
