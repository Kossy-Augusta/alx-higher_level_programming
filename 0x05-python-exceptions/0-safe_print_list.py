#!/us/bin/python3

'''
    safe_print_list - function that prints x elements of a list
    @my_list: my_list can contain any type (integer, string, etc.)
    @x: number of elements to print
    x can be bigger than the length of my_list

    Return: the real number of elements printed
'''


def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for i in range(x):
            print(my_list[i], end="")
            num += 1
        print()
        return num
    except IndexError:
        return num
