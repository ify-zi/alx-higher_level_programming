#!/usr/bin/python3
"""
    Using the post method on the Requests package
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    link = argv[1]
    info = {'email': argv[2]}
    resp = requests.post(link, data=info)
    print(resp.text)
