#!/usr/bin/python3
"""
    This module uses the Request package
    to retrive a response
"""


import requests

link = 'https://alx-intranet.hbtn.io/status'
resp = requests.get(link)
print("Body response:")
print("\t- type: {}".format(type(resp.text)))
print("\t- content: {}".format(resp.text))
