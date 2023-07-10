#!/usr/bin/python3
"""This module contains an empty class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Area function.

        Raises:
            Exception: area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

        Args:
            name (str): name of the object.
            value (int): value of the object.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
