#!/usr/bin/python3
"""write file with two arguments"""


def write_file(filename="", text=""):
    """read file name with utf-8"""
    with open(filename, "w",  encoding='utf-8') as f:
        return f.write(text)
