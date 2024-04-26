#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]
    val = {'email': email}
    r = requests.post(url, data=val)
    out = r.text

    print("Your email is:", out)
