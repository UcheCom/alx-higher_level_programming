#!/usr/bin/python3
""" Defines class LockedClass with no attribute or no class
    that prevents the user from dynamically creating
   new instance
"""


class LockedClass():
    """ New instance variable declaration """
    __slots__ = ('first_name')

    def __init__(self):
        """Init method"""
        pass
