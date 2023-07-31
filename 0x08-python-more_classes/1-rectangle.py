#!/usr/bin/python3
"""This script defines a Rectangle class."""


class Rectangle:
    """This class models a rectangle."""

    def __init__(self, width=0, height=0):
        """Constructs a Rectangle instance.

        Args:
            width (int): Defines the width of the rectangle.
            height (int): Defines the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Manage the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Manage the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
