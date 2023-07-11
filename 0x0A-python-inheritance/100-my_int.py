#!/usr/bin/python3

"""Defines the class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !=

    Args:
        int (int): value
    """
    def __init__(self, value):
        """Initializes the instance attributes.

        Args:
            value (int): integer.
        """
        self.__value = value

    def __eq__(self, other):
        """Invert the method equal to.

        Args:
            other (int): integer.

        Returns:
            bool: True or False.
        """
        return self.__value != other

    def __ne__(self, other):
        """Invert the method not equal to.

        Args:
            other (int): integer.

        Returns:
            bool: True or False
        """
        return self.__value == other
