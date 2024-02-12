#!/usr/bin/python3
"""
new classes square
"""
from models.rectangle import Rectangle 


class Square(Rectangle):
    """
    defining the class square that inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializing the class square

        Args:
        size (int): size of square
        x (int): x coordinate
        y (int): y coordinate
        id (int): identitiy of square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set/get size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """setting the size of square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute"""
        if args and len(args) != 0:
            ar = 0
            for arg in args:
                if ar == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif ar == 1:
                    self.size = arg
                elif ar == 2:
                    self.x = arg
                elif ar == 3:
                    self.y = arg
                ar += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def __str__(self):
        """returns a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size
                )
