#!/usr/bin/python3
"""
a class defining a rectangle
"""


class Rectangle:
    """
    A class representing a rectangle

    Attributes:
    number_of_instances (int): number of rectangle instances
    print_symbol (any): the symbol for representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializing a rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on area

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with equivalent width, height and size.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """
        Represents the rectangle with a #
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = [''.join([(str(self.print_symbol)) for _ in range(self.__width)]) + '\n'
                for _ in range(self.__height - 1)]
        rect.append(''.join([(str(self.print_symbol)) for _ in range(self.__width)]))
        return ''.join(rect)

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        return (f"Rectangle({self.__width}, {self.__height}.")

    def __del__(self):
        """
        prints an error message when an instance of the rectangle is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
