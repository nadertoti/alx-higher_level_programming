#!/usr/bin/python3
"""JSON representation of an object {string}"""


import json


def load_from_json_file(filename):
    """creates an object from jsom file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f)
