#!/usr/bin/python3
"""Write a function that returns an object"""


import json


def from_json_string(json_str):
    """Write a function that returns an object"""
      with open(json_str) as f:
        data = json.load(f)
    return data
