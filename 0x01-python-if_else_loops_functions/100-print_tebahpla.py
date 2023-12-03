#!/usr/bin/python3

'''
program that prints the ASCII alphabet, in reverse
order, alternating lowercase and uppercase
'''
# loop from 122 - 97
for i in range(122, 96, -1):
    if i % 2:
        i = i - 32
    print("{}".format(chr(i)), end="")
