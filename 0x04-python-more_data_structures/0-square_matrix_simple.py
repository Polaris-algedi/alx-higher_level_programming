#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix

    Args:
        matrix: 2d list of integers

    Returns:
        The new list.
    """
    return list(map(lambda row: [x**2 for x in row], matrix))
