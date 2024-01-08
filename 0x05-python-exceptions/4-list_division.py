#!/usr/bin/python3
'''
list_division - Function that divides element by element 2 lists.
@my_list_1: first list
@my_list_2: second list
@list_length: nmber of elements in the new list
If 2 elements can’t be divided, the division result should be equal to 0
Return: Returns a new list (length = list_length) with all divisions

'''


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
