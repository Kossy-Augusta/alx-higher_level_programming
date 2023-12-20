'''
    Function
    common_elements - Function that returns a set of common
    elements in two sets.

    Arguments
    @set_1 and set_2: Set of numbers
'''


def common_elements(set_1, set_2):
    common_values = set_1 & set_2
    return (common_values)
