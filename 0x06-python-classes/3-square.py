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
    def __init__(self, size=0):
        """Initialize a square object with size variable
        Args:
            size: size of the square
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Area method

        Retruns the area of the square
        """
        return self.__size ** 2
