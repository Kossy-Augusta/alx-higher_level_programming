#!/usr/bin/python3

# function that coverts lowe case to uppercase
def uppercase(str):
    for a in str:
        if ord(a) >= 97 and ord(a):
            a = chr(ord(a) - 32)
        print("{}".format(a), end="")
    print()
