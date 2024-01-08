#!/usr/bin/python3
"""
    object comparison
"""


def is_same_class(obj, a_class):
    """
        checks instance of a class
    """

    if type(obj) == a_class:
        return True
    else:
        return False
