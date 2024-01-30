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

    indent_chars = set(".?:")
    sentence = ""

    for char in text:
        sentence += char

        if char in indent_chars or char == "\n":
            print(sentence.strip())
            print()
            sentence = ""

        if sentence:
            print(sentence.strip())
