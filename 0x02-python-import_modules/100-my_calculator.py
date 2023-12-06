#!/usr/bin/python3

if __name__ == '__main__':
    import sys  # import the sys module
    from calculator_1 import add, sub, mul, div
    arguments = sys.argv  # Get the list of command line arguments
    length = len(arguments)  # get the length of the list
    if length < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    # Assighn the operator and operans to a variable
    a = int(arguments[1])
    operator = arguments[2]
    b = int(arguments[3])
    # Check if the operator value is in the lost of allowed operators
    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if operator == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif operator == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
