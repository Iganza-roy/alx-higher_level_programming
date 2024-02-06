#!/usr/bin/python3
"""
defining the load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”i
    Args:
        filename: the file to be used
    """
    with open(filename) as f:
        return (json.load(f))
