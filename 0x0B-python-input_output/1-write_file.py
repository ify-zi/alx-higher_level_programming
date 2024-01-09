#!/usr/bin/python3
"""
    Write File MOdule
"""


def write_file(filename="", text=""):
    """
        write to a file or create file
        if not exist
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
