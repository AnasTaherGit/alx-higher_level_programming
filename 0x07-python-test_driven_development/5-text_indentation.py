#!/usr/bin/python3
"""Defines a function for formatting text by introducing indentation."""


def text_indentation(input_text):
    """Displays text with two new lines after each '.', '?', and ':'.

    Args:
        input_text (string): The text to be displayed.
    Raises:
        TypeError: If input_text is not a string.
    """
    if not isinstance(input_text, str):
        raise TypeError("text must be a string")

    char_index = 0
    while char_index < len(input_text) and input_text[char_index] == ' ':
        char_index += 1

    while char_index < len(input_text):
        print(input_text[char_index], end="")
        if input_text[char_index] == "\n" or input_text[char_index] in ".?:":
            if input_text[char_index] in ".?:":
                print("\n")
            char_index += 1
            while (char_index < len(input_text) and
                    input_text[char_index] == ' '):
                char_index += 1
            continue
        char_index += 1
