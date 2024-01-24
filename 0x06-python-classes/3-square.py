#!/usr/bin/python3

"""creating a class called square."""


class Square:
    """defining a square class."""

    def __init__(self, size=0):
        """initializing a new square class with an initial value.
        Args:
            size: the size of the square; which is very crucial in computation.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """public instance method that returns the current square area"""
        return (self.__size ** 2)
