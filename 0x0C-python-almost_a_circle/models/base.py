#!/usr/bin/python3
"""
creating a class base
"""
import json


class Base:
    """
    defining the class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializing the class Base
        Args:
            id (int): argument
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
         writes the JSON string representation of list_objs to a file

         Args:
            list_objs (list): is a list of instances wich inherits of Base
        """
        fname = cls.__name__ + ".json"
        with open(fname, "w") as j:
            if list_objs is None:
                j.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                j.write(Base.to_json_string(list_dicts))
