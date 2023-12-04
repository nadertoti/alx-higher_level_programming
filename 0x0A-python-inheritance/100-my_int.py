#!/usr/bin/python3
"""Module for 2 is same class method."""


class MyInt(int):
    """new varsion of an integer."""
    def __new__(cls, *args, **kwargs):
        """version of integers good for oppsite."""
        return super(MyInt, cls,).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """new instance of class."""
        return int(self) != other

    def __ne__(self, other):
        """it was == is now."""
        return int(self) == other
