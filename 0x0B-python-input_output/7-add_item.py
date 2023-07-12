#!/usr/bin/python3
"""Examples to demonstrate how Input/Output works in python"""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


fileName = "add_item.json"
items = []

if path.exists(fileName):
    items = load_from_json_file(fileName)

items.extend(argv[1:])

save_to_json_file(items, fileName)
