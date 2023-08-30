#!/usr/bin/python3
""" Define a class Square. """


class Square:
    """ Represent a Square. """
    def __init__(self, size):
        """Initialze a new Square.
        Ags:
            size(int): The size of the new square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
