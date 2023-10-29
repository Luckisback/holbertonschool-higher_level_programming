#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list"""

import json
import os
import sys
import importlib

# Import the 'save_to_json_file' function using importlib
save_to_json_file_module = importlib.import_module('5-save_to_json_file')
save_to_json_file = save_to_json_file_module.save_to_json_file

# Import the 'load_from_json_file' function using importlib
load_from_json_file_module = importlib.import_module('6-load_from_json_file')
load_from_json_file = load_from_json_file_module.load_from_json_file

def main():
    # Get the command-line arguments (excluding the script name)
    args = sys.argv[1:]

    # Initialize existing_data to an empty list
    existing_data = []

    # If the file "add_item.json" exists, load its contents
    if os.path.exists("add_item.json"):
        try:
            existing_data = load_from_json_file("add_item.json")
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    # Add the command-line arguments to the list
    existing_data.extend(args)

    # Save the updated list to "add_item.json"
    save_to_json_file(existing_data, "add_item.json")

if __name__ == "__main__":
    main()
