#!/usr/bin/python3
"""Square module"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes instance attributes

        Args:
            size: size of the square
            position:
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Resets the position of the square

        Args:
            value: position of the square

        Raises:
            TypeError: If 'position' is not a tuple of 2 positive integers
        """
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) != int or value[0] < 0 or
                type(value[1]) != int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the square's area"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #.
        If size is equal to 0, print an empty line.
        Position should be use by using space.
        Don’t fill lines by spaces when position[1] > 0
        """
        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end='')

            for k in range(self.__size):
                print("#", end='')
            print()
