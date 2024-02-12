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

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string

        Args:
            json_string (str): string representing a list of dictionaries
        """
        if  json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        fname = str(cls.__name__) + ".json"
        try:
            with open(fname, "r") as j:
                list_dict = Base.from_json_string(j.read())
                return [cls.create(**i) for i in list_dict]
        except IOError:
            return []
