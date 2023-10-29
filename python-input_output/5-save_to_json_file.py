#!/usr/bin/python3
"""Write a function tha creats an objet in a file with json"""


import json


def save_to_json_file(my_obj, filename)::
    """A function that save in json format"""
      with open(filename, 'w', encoding='utf8') as f:
        json.dump(my_obj, f)