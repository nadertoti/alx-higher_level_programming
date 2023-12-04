#!/usr/bin/python3
"""Function that add attribute to object."""


def add_attribute(obj, att, value):
    """Push a new attribute to an object if possible.

    Args:
        obj (any): Add object to add attribute.
        att (str): Name of the attribute to add obj.
        value (any): Value of att.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
