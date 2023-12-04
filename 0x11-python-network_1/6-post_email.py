#!/usr/bin/python3
"""Sends a POST request with an email passed as parameter"""
import requests
import sys


if __name__ == '__main__':
    url1 = sys.argv[1]
    url2 = sys.argv[2]
    try:
        page = requests.post(url1, data={'email': url2})
        print(page.text)
    except Exception:
        pass
