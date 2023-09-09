#!/usr/bin/python3

"""
Defines a function tthat prints a text
with 2 new lines after ., ? and : characters.
"""


def text_indentation(text):
    """
      prints a text with 2 new lines after
      ., ?, and : characters

      Args:
          text: str
      Returns:
             Nothing
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delm in ".:?":
        text = (delm + "\n\n").join(
            [line.strip(" ") for line in text.split(delm)])

    print("{}".format(text), end="")
