#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.

The function, 'matrix_divided(matrix, div)', takes two arguments,
'matrix' and 'div', and returns a new matrix that contains
the dividision of all elements of the 'matrix' by 'div'.
All elements of the matrix should be divided by div,
rounded to 2 decimal places.

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Elements of the matrix must be integers or floats,
    same for the divisor.

    Args:
        matrix (list): The list of lists of integers or floats.
        div (int or float): The divisor.

    Raises:
        TypeError: If the matrix is not a list of lists
                   of integers or floats.
                   If the rows of the matrix doesn't
                   have the same size.
                   If div is not a number (integer or float).

        ZeroDivisionError: If div equals 0.

    Returns:
        list: The new matrix.
    """

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    mxTypeErr = "matrix must be a matrix (list of lists) of integers/floats"
    mxSizeErr = "Each row of the matrix must have the same size"

    if type(matrix) != list or not matrix:
        raise TypeError(mxTypeErr)

    rowLen = 0
    newMatrix = []
    for row in matrix:
        if type(row) != list or not row:
            raise TypeError(mxTypeErr)

        if rowLen != 0 and len(row) != rowLen:
            raise TypeError(mxSizeErr)

        newRow = []
        for num in row:
            if type(num) not in (int, float):
                raise TypeError(mxTypeErr)

            newRow.append(round(num / div, 2))

        newMatrix.append(newRow)
        rowLen = len(row)

    return (newMatrix)
