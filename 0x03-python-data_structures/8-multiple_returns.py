#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length of a string
    and its first character.

    Description:
        If a tuple is smaller than 2,
        use the value 0 for each missing integer.
        If a tuple is bigger than 2,
        use only the first 2 integers.

    Args:
        sentence: string

    Returns:
            A tuple with the length of a string
            and its first character.
    """
    length = len(sentence)
    first_char = None if length == 0 else sentence[0]
    return (length, first_char)
