#!/usr/bin/python3
"""
    This defines a functions that prints a square with the
    character #.

"""


def print_square(size):
    """
       Prints a square wiht the character #
       Args:
           size: length of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
