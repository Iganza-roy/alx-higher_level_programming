#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays
the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    err = r.status_code

    if err >= 400:
        print("Error code:", err)
    else:
        print(r.text)
