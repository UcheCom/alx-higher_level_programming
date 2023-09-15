#!/usr/bin/python3
"""This defines a text insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """This inserts a line of text to a file after each
       line containing a string

       Args:
           filename: The name of the file
           search_string: The string to search for in the file
           new_string: new string to be inserted
    """
    text = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            text.append(line)
            if search_string in line:
                text.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
