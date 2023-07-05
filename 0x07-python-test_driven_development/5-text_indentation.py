#!/usr/bin/python3
"""
This module provides a function that prints a new line after ., ? and :.

The function, 'text_indentation(text)', takes
a string as argument, 'text', and prints
the text after modifying it.

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: text to indent

    Raises:
        TypeError: If text is not a string

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    cpText = text[:]
    cpText = cpText.strip()
    for i in range(len(cpText)):
        if i != 0 and cpText[i - 1] in [".", "?", ":"]: 
            continue
        
        print(cpText[i], end="")
        if cpText[i] in [".", "?", ":"]:
            print("\n")
         
