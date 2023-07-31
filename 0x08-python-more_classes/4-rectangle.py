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

    def area(self):
        """Calculates the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Generates a printable string representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Generates a formal string representation of the Rectangle."""
        rect_str = "Rectangle(" + str(self.__width)
        rect_str += ", " + str(self.__height) + ")"
        return (rect_str)
