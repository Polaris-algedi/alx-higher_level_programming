#!/usr/bin/python3
"""This module contains the class MyList that inherits from list."""


class MyList(list):
    """Class that inherits from list.

    Args:
        list (list): list to sort in ascending order.
    """
    def print_sorted(self):
        """Prints a list in ascending order."""
        myList = self[:]
        myList.sort()
        print(myList)
