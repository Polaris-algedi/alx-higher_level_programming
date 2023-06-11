#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

    Args:
        matrix: 2D list
    """
    for item in matrix:
        for i, number in enumerate(item):
            print("{}".format(number), end="")
            print("\n" if i == len(item) - 1 else " ", end="")
