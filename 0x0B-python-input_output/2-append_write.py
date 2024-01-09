#!/usr/bin/python3
"""
    Append Write File Module
"""


def append_write(filename="", text=""):
    """
        appendd to the end of a file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
