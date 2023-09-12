#!/usr/bin/python3
"""Defines scripts that add all argument to a a Python
   list and save them to a file
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

_list = []
if os.path.exists('add_item.json'):
    _list = load_from_json_file('add_item.json')

for arg in sys.argv[1:]:
    _list.append(arg)

save_to_json_file(_list, 'add_item.json')
