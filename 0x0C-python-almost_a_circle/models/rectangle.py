#!/usr/bin/python3
""" Class Rectangle """
from models.base import Base


class Rectangle(Base):
    """
        Defines the Rectangle class
        Inherited from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This returns the area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """
            Prints to stdout the representation of the rectangle
        """
        rect = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rect += (" " * self.x) + ("#" * self.width) + "\n"
        print(rect, end="")

    def update(self, *args, **kwargs):
        """
            This updates the arguments in the class
        """
        if args is not None and len(args) != 0:
            _listattr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, _listattr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This returns a dictn with attributes"""
        _listattr = ['id', 'width', 'height', 'x', 'y']
        dictn = {}
        for key in _listattr:
            dictn[key] = getattr(self, key)

        return dictn
