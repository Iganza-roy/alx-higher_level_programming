#!/usr/bin/python3
"""
creating a function that adds two integers
a and b must be integers or floats
a and b must be first casted to integers if they are float
"""


def add_integer(a, b=98):
    """
    defining a function that adds two integers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    result = a + b
    return int(result)
