#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Function that prints all integers of a list

    Args:
        my_list: list of integers
    """
    if my_list:
        for number in my_list:
            print("{:d}".format(number))
