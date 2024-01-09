#!/usr/bin/python3
"""
    file I/O Module
"""


def read_file(filename=""):
    """
        return content of a file
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
