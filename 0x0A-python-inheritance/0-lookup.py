#!/usr/bin/python3
"""Module for lookup method."""


def lookup(obj):
    """looks up objects attributes and approuach

    Args:
        obj (_type_): _description_

    Returns:
        list: list of attributes.
    """
    return dir(obj)
