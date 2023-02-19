#!/usr/bin/python3
"""Function read_file"""


def read_file(filename=""):
    """Open file simple reading"""

    with open(filename, "r") as fichier:
        fichier = fichier.read()
        print(fichier, end="")
