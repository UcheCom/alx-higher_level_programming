#!/usr/bin/python3
"""Defines a fucntion that check if
   an instance belong to a class or it subclass
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class
       or it subclass

       Args:
           obj: object
           a_class: a class

       Return:
             True or False
    """
    if isinstance(obj, a_class):
        return True
    return False
