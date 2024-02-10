#!/usr/bin/python3
"""
class rectangle that inherits from base
"""


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
