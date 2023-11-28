#!/usr/bin/python3
"""Defines a class LockedClass"""


class LockedClass:
    """
    Did not allow user from add different name attribute.
    
    Attributes:
        first_name (str): first name.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates a new class."""

        self.first_name = "first_name"
