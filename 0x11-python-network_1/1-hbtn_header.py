#!/usr/bin/python3
"""
    This module uses the urllib and sys package
    to return the X-request-id by taking the url passed
"""


if __name__ == '__main__':
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as resp:
        print(resp.headers.get('X-request-id'))
