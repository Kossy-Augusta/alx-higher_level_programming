#!/usr/bin/python3
# define a function is lower that returns true if a character is lowercase
def islower(c):
    if ord(c) >= 96 and ord(c) <= 122:
        return True
    else:
        return False
