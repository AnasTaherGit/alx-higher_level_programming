#!/usr/bin/python3
"""Defines a secured class."""


class LockedClass:
    """
    Restricts the user from creating new LockedClass attributes
    except for an attribute named 'primary_name'.
    """

    __slots__ = ["first_name"]
