#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    args = sys.argv
    length = len(args)
    total = 0
    if length == 1:
        print(total)
        sys.exit()
    for i in args[1: length + 1]:
        total += int(i)
    print("{:d}".format(total))
