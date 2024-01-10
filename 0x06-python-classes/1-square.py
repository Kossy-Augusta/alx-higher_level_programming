#!/usr/bin/python3

"""1-square.py

Just a simple module


Atrributes: Square: A class
"""


class Square:
    """Square class

    represents a square


    Attributes:
        size(int): size of the square
    """
    def __init__(self, size):
        """Initialize a square object with size variable
        Args:
            size: size of the square
        """
        self.__size = size
