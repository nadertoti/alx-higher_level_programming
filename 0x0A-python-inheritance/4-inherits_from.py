#!/usr/bin/python3
"""Module for 2 is same class method."""


def inherits_from(obj, a_class):
    """Calculate if  an object is a true subclass of a class."""
    return isinstance(obj, a_class) and type(obj) != a_class
