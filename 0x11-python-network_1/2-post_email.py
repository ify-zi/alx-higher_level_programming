#!/usr/bin/python3
"""
    Using a post request to geta response from the url
    while passing a parameter as email
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    from sys import argv

    link = argv[1]
    param = {'email': argv[2]}
    param = urllib.parse.urlencode(param)
    param = param.encode('utf-8')
    with urllib.request.urlopen(link, param) as resp:
        msg = resp.read()
        print(msg)
