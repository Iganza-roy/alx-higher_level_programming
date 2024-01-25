#!/usr/bin/python3

"""creating a class called square"""


class Square:
    """defining a square class"""

    def __init__(self, size=0):
        """initializing a new square class with an initial value
        Args:
            size: the size of the square; which is very crucial in computation.
            size must be an integer and greater than 0
        """
        self.size = size

    @property
    def size(self):
        """set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """public instance method that returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """public instance method that prints in stdout the square
        with the character #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
