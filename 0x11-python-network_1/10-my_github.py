#!/usr/bin/python3
"""
    Script takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    resp = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    try:
        print(resp.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
