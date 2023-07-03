#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes instance attributes.

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): width of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value: height of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Create an 'informal' and nicely printable string
        representation of the rectangle instance
        """
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        for i in range(self.__height):
            rect += '#' * self.__width + "\n"
        return rect

    def __repr__(self):
        """Create an 'official' string representation of
        the rectangle instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of the rectangle class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
