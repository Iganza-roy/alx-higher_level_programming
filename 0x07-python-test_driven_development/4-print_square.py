#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    """defining the print_square function

    Args:
        size (int): The height/width of the square.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
