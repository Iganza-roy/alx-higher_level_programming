#!/usr/bin/python3

class Square:
    """Defining a class called square"""

    def __init__(self, size):
        """initializing a new square class with an initial value
        for attributes
        Args:
            size: the size of the square; which is very crucial in computation.
            It is therefore set as a private attribute
        """
        self.__size = size
