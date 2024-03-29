#!/usr/bin/python3
"""
    Error handling on Request package
    Script returns error codes greater than 400
"""


if __name__ == '__main__':
    import requests
    from sys import argv


    resp = requests.get(argv[1])
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
