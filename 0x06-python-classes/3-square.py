#!/usr/bin/python3
"""Square module"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes instance attributes

        Args:
            size: size of the square

        Raises:
            TypeError: If 'size' is not an integer
            ValueError: If 'size' is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate the square's area"""
        return self.__size ** 2
