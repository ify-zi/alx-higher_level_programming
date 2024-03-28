#!/usr/bin/python3
"""
    This module handles the error msg
    from http using the status code
"""


if __name__ == '__main__':
    import urllib.request
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as resp:
            print(resp.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
