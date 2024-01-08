#!/usr/bin/python3
"""
    add_attribute Module
"""


def add_attribute(a_class, name, value):
    """
        add attributes to a class
    """
    a_class.name = value
    if getattr(a_class, name, value):
        pass
    else:
        raise TypeError("can't add new attribute")
