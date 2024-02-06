#!/usr/bin/python3
"""
Defines a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    Custom integer class that inverts == and != operators.
    """

    def __eq__(self, value):
        """
        Override == operator to compare inequality.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Override != operator to compare equality.
        """
        return self.real == value
