#!/usr/bin/python3
"""
    JSON to python Object
"""


import json


def from_json_string(my_str):
    """
        decode json to python object
    """
    return json.loads(my_str)
