#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """ This intializes a new Rectangle.

        Args:
            width: The width of the new Rectangle.
            height: The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """This returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This returns a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
