#!/usr/bin/python3
"""
    this Script retrive a json file from
    the requests get method
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    t_url = "http://0.0.0.0:5000/search_user"
    dat = {"q": argv[1][0] if len(argv) > 1 else ""}
    resp= requests.post(t_url, data=dat)
    try:
        f_resp = resp.json()
        if not f_resp:
            print("No result")
        else:
            print("[{}]: {}".format(f_resp.get("id"), f_resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
