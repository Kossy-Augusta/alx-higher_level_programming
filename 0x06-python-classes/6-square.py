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
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square object with size variable
        Args:
            size: size of the square
            position: Position argument
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size

        Function to retrieve the value of private attribute __size
        """
        return self.__size

    @property
    def position(self):
        """Postion

        Funtion returns the value of the private attribute position
        """
        return self.__position

    @size.setter
    def size(self, size):
        """Size

        Function to set the value of __size

        Args:
            size: value of size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @position.setter
    def position(self, value):
        """sets the position of the square if a tuple of positive integars\
                is passed in"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(map(lambda x: x >= 0, value))):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Area method

        Retruns the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with character #"""
        if self.__size == 0:
            print()
            return

        [print() for space in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for space in range(self.position[0])]
            [print("#", end="") for j in range(self.__size)]
            print()
