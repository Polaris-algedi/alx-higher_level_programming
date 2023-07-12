#!/usr/bin/python3
"""Examples to demonstrate how Input/Output works in python"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student.

        If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.

        Args:
            attrs (list): List of attributes to represent.
        """
        if (isinstance(attrs, list) and
                all(isinstance(item, str) for item in attrs)):
            return {at: getattr(self, at) for at in attrs if hasattr(self, at)}
        return self.__dict__
