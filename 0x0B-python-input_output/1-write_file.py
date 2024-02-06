#!/usr/bin/python3
"""
a function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    defining the write_file function
    """
    with open(filename, "w", encoding="uft-8") as f:
        """
        this writes a string to a UTF8 text file.
        Args:
            filename (str): Is the name of the file to write.
            text (str): Is the text to write to the file.
        """
        return (f.write(text))
