#!/usr/bin/python3
""" takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    var = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=var)

    try:
        resp = r.json()

        if resp:
            print("[{}] {}".format(resp['id'], resp['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
