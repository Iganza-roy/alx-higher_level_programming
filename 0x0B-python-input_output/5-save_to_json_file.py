#!/usr/bin/python3
"""
defining the save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation:
    Args:
        my_obj - object to be written
        filename - textfile to be written onto
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
