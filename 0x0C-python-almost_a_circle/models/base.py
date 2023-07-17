#!/usr/bin/python3
"""Module that contains the Base class and related methods
for serialization and deserialization."""
import json


class Base:
    """Base class with serialization and deserialization functionality."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instances of the Base class with a unique identifier."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string representation."""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of object instances to a JSON file."""
        js = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as f:
            f.write(js)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string representation to a list of dictionaries."""
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of the class based on a dictionary
        of attributes."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a JSON file."""
        try:
            filename = f"{cls.__name__}.json"
            with open(filename, 'r') as f:
                d = cls.from_json_string(f.read())
            return [cls.create(**x) for x in d]
        except FileNotFoundError:
            return []
