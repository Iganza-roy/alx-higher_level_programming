#!/usr/bin/python3
"""
Write a function that returns the JSON
representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """
    defining the function
    Parameters:
    - my_obj: The Python object to be converted.
    """
    return (json.dumps(my_obj))
