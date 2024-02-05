#!/usr/bin/python3
"""
class basegeometry
"""


class BaseGeometry:
    """
    defining the class
    """
    def area(self):
        """
        raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instannce method that validates value
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
