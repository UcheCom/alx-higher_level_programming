#!/usr/bin/python3
"""Defines a function that appends a text to a textfile"""


def append_write(filename="", text=""):
    """Append a text to a text file

       Args:
           filename: filename/path
           text: string to be written

       Return:
             The number of text appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
