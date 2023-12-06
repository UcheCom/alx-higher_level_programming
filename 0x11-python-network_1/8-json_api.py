#!/usr/bin/python3
"""This sends a POST request to http://0.0.0.0:5000/search_user
with a given letter.
Usage: ./8-json_api.py <letter>
  - The letter is sent the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests


if __name__ == '__main__':
    letter = {'q': ""}
    try:
        letter['q'] = sys.argv[1]
    except Exception:
        pass

    r = requests.post("http://0.0.0.0:5000/search_user", letter)
    try:
        resp = r.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp["id"], resp["name"]))
    except ValueError:
        print("Not a valid JSON")
