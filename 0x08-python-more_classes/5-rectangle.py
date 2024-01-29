#!/usr/bin/python3
"""
a class defining a rectangle
"""


class Rectangle:
    """A class representing a rectangle"""
    def __init__(self, width=0, height=0):
        """initializing a rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """setting the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        public instance method that returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        public instance method that that returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Represents the rectangle with a #
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = [''.join(['#' for _ in range(self.__width)]) + '\n'
                for _ in range(self.__height - 1)]
        rect.append(''.join(['#' for _ in range(self.__width)]))
        return ''.join(rect)

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        return (f"Rectangle({self.__width}, {self.__height}.")

    def __del__(self):
        """
        prints an error message when an instance of the rectangle is deleted
        """
        print("Bye rectangle...")
