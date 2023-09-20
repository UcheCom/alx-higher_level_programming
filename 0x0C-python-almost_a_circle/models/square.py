#!/usr/bin/python3
"""This is square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """This initializes the attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This returns a string representation of a square"""
        s = "[Square] ({}) {}/{} - ".format(self.id, self.x, self.y)
        s_1 = "{}".format(self.width)
        return (s + s_1)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This assigns attributes"""
        if args is not None and len(args) != 0:
            _listattr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if _listattr[i] == 'size':
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, _listattr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        _listattr = ['id', 'size', 'x', 'y']
        dictn = {}

        for key in _listattr:
            if key == 'size':
                dictn[key] = getattr(self, 'width')
            else:
                dictn[key] = getattr(self, key)

        return (dictn)
