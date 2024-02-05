#!/usr/bin/python3
"""
a function that returns True if the object is exactly an instance
of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    defining the function
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    """
    if type(obj) == a_class:
        return True
    return False
