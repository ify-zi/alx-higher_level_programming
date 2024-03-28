#!/usr/bin/python3
"""
    Using the requet package to retrieve
    X-request-id
"""


if __name__ == '__main__':
    import requests
    import sys

    link = sys.argv[1]
    resp = requests.get(link)
    print(resp.headers.get('X-Request-Id'))
