#!/usr/bin/python3
"""
defining a class student
"""


class Student:
    """
    a student class defined by public instance attributes
    """
    def __init__(self, first_name, last_name, age):
        """
        initializing the class student
        Args:
            first_name(str): first name
            last_name(str): last name
            age(int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        Args:
            attrs (list): attributes to represent
        """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return (self.__dict__)

    def reload_from_json(self, json):
        """
        function that replaces all attributes of the Student instance.
        Args:
            json (dict): key/value pairs to replace attributes with
        """
        for j, i in json.items():
            setattr(self, j, i)
