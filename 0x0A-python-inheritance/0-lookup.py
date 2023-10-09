#!/usr/bin/python3
"""Specifies a function that looks up object attributes."""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return dir(obj)
