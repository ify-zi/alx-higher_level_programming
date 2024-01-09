#!/usr/bin/python3
"""
    LOAD FROM JSON FILE
"""


import json


def load_from_json_file(filename):
    """
        load from json file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
