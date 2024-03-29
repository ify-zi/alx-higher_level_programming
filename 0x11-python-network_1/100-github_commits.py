#!/usr/bin/python3
"""
    script return users who commited to a repo
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    resp = requests.get("https://api.github.com/repos/{}/{}/commits"
                        .format(owner, repo))
    committers = resp.json()
    for committer in committers[:10]:
        print(committer.get("sha"), end=": ")
        print(committer.get('commit').get("author").get("name"))
