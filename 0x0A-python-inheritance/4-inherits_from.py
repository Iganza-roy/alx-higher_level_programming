#!/usr/bin/python3
"""
a function that returns True if the object
is an instance of a class that inherited
(directly or indirectly) from the specified
class ; otherwise False.
"""
def inherits_from(obj, a_class):
    """
    defining the function
    Args:
        obj (any): This is the object to check.
        a_class (type): This is the class to match the type of obj to.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
