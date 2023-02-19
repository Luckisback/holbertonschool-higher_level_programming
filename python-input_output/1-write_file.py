#!/usr/bin/python3
"""function write_file"""


def write_file(filename="", text=""):
    """Write file Return number of characters"""

    with open(filename, "w") as fichier:
        fichier.write(text)
        return len(text)
