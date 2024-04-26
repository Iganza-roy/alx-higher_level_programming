#!/usr/bin/python3
"""takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import sys

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]
    #email_enc = email.encode('utf-8')
    req = urllib.request.Request(url, data=email.encode('utf-8'), method='POST')
    with urllib.request.urlopen(req) as response:
        req_data = response.read().decode('utf-8')
    print(req_data)
