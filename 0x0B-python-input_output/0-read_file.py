#!/usr/bin/python3
"""Defines a function that reads a text file and
   prints it to stdout
"""


def read_file(filename=""):
    """prints the contents of UTF8 text file to stdout.

       Args:
           filename: filename/path
    """

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
