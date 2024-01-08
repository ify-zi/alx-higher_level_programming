#!/usr/bin/python3
"""
    checks for sub class
"""


def inherits_from(obj, a_class):
    """checks if obj is subcalss"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
