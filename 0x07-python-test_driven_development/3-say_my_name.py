#!/usr/bin/python3
"""This module contains a function for printing personal names."""


def say_my_name(first_name, surname=""):
    """Display a formatted name.

    Args:
        given_name (str): The personal name to be displayed.
        surname (str): The family name to be displayed.
    Raises:
        TypeError: If either given_name or surname are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(surname, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, surname))
