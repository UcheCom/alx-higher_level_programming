#!/usr/bin/python3
"""This defines a method to set an attribute to an
   object if possible
"""


def add_attribute(obj, name, value):
    """This sets an attribute to mc if possible

       Args:
           obj: The object to add an attribute to.
           name: attribute name to add to obj.
           value: attribute value.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
