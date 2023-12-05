#!/usr/bin/python3
"""Write Student class that defines a studant"""


class Student:
    """Display of a studant"""
    def __init__(self, first_name, last_name, age):
        """Initializes the studant."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary of a studant instance."""
        return self.__dict__
