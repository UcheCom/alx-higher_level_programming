#!/usr/bin/python3
"""This defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a class

       Args:
           obj: object
           a_class: a class

       Return:
             True or False
    """
    if type(obj) == a_class:
        return True
    return False
