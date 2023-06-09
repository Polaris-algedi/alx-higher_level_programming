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

    def my_print(self):
        """Prints in stdout the square with the character #.
        If size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
