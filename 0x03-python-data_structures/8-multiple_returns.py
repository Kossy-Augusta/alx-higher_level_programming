#!/usr/bin/python3

'''
    Function
    multiple_returns - Function that returns a tuple
    with the length of a string and its first character

    Arguments
    @sentence: A string

    Return: a tuple that contains the length of a string
    and it's first character

'''


def multiple_returns(sentence):
    len_sentence = len(sentence)
    if sentence == "":
        first_char = None
    else:
        first_char = sentence[0]
    new_tuple = (len_sentence, first_char)

    return (new_tuple)
