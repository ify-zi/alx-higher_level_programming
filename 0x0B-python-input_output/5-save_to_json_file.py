#!/usr/bin/python3
"""
    Write JSON to file
"""


import json


def save_to_json_file(my_obj, filename):
    """
        create JSON and save to file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
