#!/usr/bin/python3
"""This module contains a function to render a square using the # symbol."""


def print_square(size):
    """Display a square shape using the # character.

    Args:
        size (int): The height/width of the square to be printed.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for idx in range(size):
        [print("#", end="") for jdx in range(size)]
        print("")
