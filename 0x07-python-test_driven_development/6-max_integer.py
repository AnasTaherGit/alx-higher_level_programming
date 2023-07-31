#!/usr/bin/python3
"""Module to identify the maximum value within a list."""


def max_integer(input_list=[]):
    """Function to locate and return the maximum integer in a list.
       If the list is devoid of elements, the function returns None.
    """
    if len(input_list) == 0:
        return None
    max_value = input_list[0]
    idx = 1
    while idx < len(input_list):
        if input_list[idx] > max_value:
            max_value = input_list[idx]
        idx += 1
    return max_value
