#!/usr/bin/python3
"""Defines a function to perform element-wise division on a matrix."""


def matrix_divided(input_matrix, divisor):
    """Performs division operation on all elements of the input matrix.

    Args:
        input_matrix (list): A list of lists containing integers or floats.
        divisor (int/float): The number to divide by.
    Raises:
        TypeError: If the input_matrix contains non-numerical elements.
        TypeError: If the input_matrix contains rows of varying sizes.
        TypeError: If divisor is neither an int nor a float.
        ZeroDivisionError: If divisor is 0.
    Returns:
        A new matrix representing the division result of all elements in the
        input matrix.
    """
    if (not isinstance(input_matrix, list) or input_matrix == [] or
            not all(isinstance(row, list) for row in input_matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in input_matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")

    if not all(len(row) == len(input_matrix[0]) for row in input_matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(divisor, int) and not isinstance(divisor, float):
        raise TypeError("div must be a number")

    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / divisor, 2), row)) for row in
             input_matrix])
