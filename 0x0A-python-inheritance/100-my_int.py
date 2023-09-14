#!/usr/bin/python3
"""This defines a class MyInt that inherits from int."""


class MyInt(int):
    """This inverts int operators == and !=."""

    def __eq__(self, value):
        """This overrides == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """This overrides != operator with == behavior."""
