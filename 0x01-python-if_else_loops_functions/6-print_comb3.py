#!/usr/bin/python3
# loop from 0 to 8
for a in range(0, 9):
    # loop from 1 - 9
    for b in range(a + 1, 10):
        if a == 8 and b == 9:
            print("{}{}".format(a, b))
        else:
            print("{}{}, ".format(a, b), end="")
