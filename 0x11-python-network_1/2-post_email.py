#!/usr/bin/python3
""" Script sends a post request and displays the body of the response"""
import sys
from urllib import request, parse


if __name__ == '__main__':
    url = sys.argv[1]
    values = {
        'email': sys.argv[2]
    }
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        page = response.read()
        print(page.decode('utf-8'))
