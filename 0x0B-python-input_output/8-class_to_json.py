#!/usr/bin/python3
"""
    Module that returns the dictionary description
"""


def class_to_json(obj):
    """
        returns the dictionary description of an obj 
    """

    my_dict = {}
    if hasattr(obj, "__dict__"):
        my_dict = obj.__dict__.copy()
    return my_dict
