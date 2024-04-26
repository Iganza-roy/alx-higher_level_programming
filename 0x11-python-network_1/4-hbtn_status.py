#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    out = r.text
    print("Body response:")
    print("\t- type:", type(out))
    print("\t- content:", out)
