#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    arguments = sys.argv
    length = len(arguments)
    if length == 1:
        print("{:d} arguments.".format(length - 1))
    else:
        if length == 2:
            print("{:d} argument:".format(length - 1))
        else:
            print("{:d} arguments:".format(length - 1))
        i = 1
        for element in arguments[1:]:
            print("{:d}: {:s}".format(i, element))
            i += 1
