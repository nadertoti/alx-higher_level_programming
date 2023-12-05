#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """read file name with utf-8"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
