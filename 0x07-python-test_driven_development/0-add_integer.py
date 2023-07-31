#!/usr/bin/python3
"""This script describes a function for computing the sum of two integers."""


def add_integer(a, b=98):
    """Returns the result of the addition operation for two numbers.

    In case of float type arguments, they are converted to integers before
    the addition operation is performed.

    Raises:
        TypeError: If either of a or b is not an integer or a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
