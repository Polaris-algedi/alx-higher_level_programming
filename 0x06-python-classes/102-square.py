#!/usr/bin/python3
"""Square module"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes instance attributes

        Args:
            size: size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Resets the size of the square

        Args:
            value: size of the square

        Raises:
            TypeError: If 'size' is not an integer
            ValueError: If 'size' is less than 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the square's area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Compares the equality of two instances"""
        return self.__size == other.__size

    def __lt__(self, other):
        """Compares if this instance is less than the other"""
        return self.__size < other.__size

    def __gt__(self, other):
        """Compares if this instance is greater than the other"""
        return self.__size > other.__size

    def __le__(self, other):
        """Compares if this instance is less than or equal to the other"""
        return self.__size <= other.__size

    def __ge__(self, other):
        """Compares if this instance is greater than or equal to the other"""
        return self.__size >= other.__size

    def __ne__(self, other):
        """Compares if this instance is not equal to the other"""
        return self.__size != other.__size
