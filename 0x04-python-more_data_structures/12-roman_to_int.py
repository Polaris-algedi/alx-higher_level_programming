#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer

    Args:
        roman_string: a roman number as a string

    Returns:
        The corresponding integer, otherwise 0
    """
    if type(roman_string) != str:
        return 0

    first_digit = roman_string[-1]
    my_sum = 0
    roman_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    for i in reversed(roman_string):
        if roman_int[i] < roman_int[first_digit]:
            my_sum -= roman_int[i]
        else:
            my_sum += roman_int[i]
        first_digit = i

    return my_sum
