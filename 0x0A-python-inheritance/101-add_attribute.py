#!/usr/bin/python3
"""
    add_attribute Module
"""


def add_attribute(a_class, name, value):
    """
        add attributes to a class
    """
    if not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(a_class, name, value)
