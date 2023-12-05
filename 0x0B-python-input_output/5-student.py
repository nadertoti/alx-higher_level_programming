#!/usr/bin/python3
"""JSON representation of an object {string}"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to text files"""
    with open(filename, "w",  encoding='utf-8') as f:
        return json.dumps(my_obj, f)
