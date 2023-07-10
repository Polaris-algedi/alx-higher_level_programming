#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def __init__(self, width, height):
        """Initializes the instance attributes.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Create an 'informal' and nicely printable string
        representation of the rectangle instance
        """
        string = f"[{str(self.__class__.__name__)}] "
        string += f"{str(self.__width)}/{str(self.__height)}"
        return string
