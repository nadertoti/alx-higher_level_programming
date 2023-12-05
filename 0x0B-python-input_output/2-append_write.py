#!/usr/bin/python3
"""appends a string at the end of the text file"""


def append_write(filename="", text=""):
    """read file name with utf-8"""
    with open(filename, "a",  encoding='utf-8') as f:
        return f.write(text)
