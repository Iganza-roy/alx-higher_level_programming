#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    cred = (username, password)

    r = requests.get("https://api.github.com/user", auth=cred)

    if r.status_code == 200:
        u_id = r.json().get("id")
        print(u_id)
