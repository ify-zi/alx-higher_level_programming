#!/usr/bin/python3
"""
    This Module uses the urlib package
"""

import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    msg = resp.read()
    print('Body response:')
    print("\t- type: {}".format(type(msg)))
    print("\t- content: {}".format(msg))
    print("\t- utf8 content: {}".format(msg.decode('utf-8')))
