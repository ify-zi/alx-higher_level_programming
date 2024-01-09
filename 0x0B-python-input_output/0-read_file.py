#!/usr/bin/python3
"""
    file I/O Module
"""


def read_file(filename=""):
    """
        return content of a file
    """
    with open(filename, encoding="utf-8") as f:
        return f.read()
