#!/usr/bin/python3
"""creating a class called square"""


class Square:
    """defining a square class"""

    def __init__(self, size):
        """initializing a new square class with an initial value
        Args:
            size: the size of the square; which is very crucial in computation.
            size must be an integer and greater than 0
        """
        if not isinstance(self, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
