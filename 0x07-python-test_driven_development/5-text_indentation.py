#!/usr/bin/python3

"""Defines a text-indentation function."""

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.
        
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indent_char = set(".?:")
    sentence = ""

    for char in text:
        sentence += char

        if char in indent_char or char == "\n":
            print(sentence.strip())
            print()
            sentence = ""
        elif char.isspace():  # Check for spaces
            continue

    if sentence:
        print(sentence.strip())
