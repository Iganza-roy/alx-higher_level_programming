#!/usr/bin/python3
"""
class rectangle that inherits from base
"""
from models.base import Base


class Rectangle(Base):
    """
    defining the class rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializing the Rectangle class
        Args:
            width (int): width of rectangle
            height (int): height of rectanle
            x (int): x coordinate of rectangle
            y (int): y coordinate of rectangle
            id (int): identity of rectangle
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """
            decorator - creating the getter/setter of width
            """
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """
            decorator - creating the getter/setter of height
            """
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """
            decorator - creating the getter/setter of x
            """
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """
            decorator - creating the getter/setter of y
            """
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
