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
        self.size = size

    @property
    def size(self):
        """Size

        Function to retrieve the value of private attribute __size
        """
        return self.__size

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

    def area(self):
        """Area method

        Retruns the area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Defines the equal == comparison method
            Returns True if objects are equal or Fale if otherwise
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the inequality function"""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Defines the > comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= comparison"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Defines the < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison"""
        return self.area() <= other.area()
