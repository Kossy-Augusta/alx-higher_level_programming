#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines a suqare"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square

        Args:
            size(int): size of the square
            position(tuple): Positional cordinate of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the value of the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get the position variable"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the positon of the position variable"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value)
                or not all(x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return sel.__size ** 2

    def my_print(self):
        """Print the square with character #"""
        result = ""
        if self.__size == 0:
            result += "\n"
            return result
        result += "\n" * self.__position[1]
        for i in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size
            result += "\n"
        return result

    def __str__(self):
        """Printing a square instance"""
        return self.my_print()
