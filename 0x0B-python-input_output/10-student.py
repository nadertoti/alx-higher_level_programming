#!/usr/bin/python3
"""Write Student class that defines a studant"""


class Student:
    """Display of a studant"""
    def __init__(self, first_name, last_name, age):
        """Initializes the studant."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns  a dictionary representation of a Student
        instance (same as 8-class_to_json.py)."""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attr:
                my_dict[key] = value
        return my_dict
