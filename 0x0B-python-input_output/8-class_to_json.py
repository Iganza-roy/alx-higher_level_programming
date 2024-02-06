#!/usr/bin/python3
"""
defining the class_to_json function
"""


def class_to_json(obj):
    """
    a function that returns the dictionary description with
    simple data structure
    Args:
        obj - instance of a class
    """
    return (obj.__dict__)
