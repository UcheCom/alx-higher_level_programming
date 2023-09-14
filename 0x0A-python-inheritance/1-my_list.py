#!/usr/bin/python3
"""Defines a module that inherits from the list class"""


class MyList(list):
    """This is a class that inherits from list"""
    def print_sorted(self):
        """This prints a sorted list in ascending order"""
        print(sorted(self))
