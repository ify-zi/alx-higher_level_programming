#!/usr/bin/python3
"""
    Write JSON to file
"""


import json


def save_to_json_file(my_obj, filename):
    """
        create JSON and save to file
    """
    json_file = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json_file)
