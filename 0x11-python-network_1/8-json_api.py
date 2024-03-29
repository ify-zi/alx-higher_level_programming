#!/usr/bin/python3
"""
    this Script retrive a json file from
    the requests get method
"""


if __name__ == '___main__':
    import requests
    from sys import argv

    q = argv[2]
    resp = requests.post(argv[1], data=q)
    f_resp = resp.json()
    if f_resp is None:
        print("No result")
    if f_resp == isinstance(json()):
        print("[{}]: {}".format(f_resp['id'], f_resp['name']))
    else:
        print("Not a valid JSON")
