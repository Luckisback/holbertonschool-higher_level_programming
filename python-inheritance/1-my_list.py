#!/usr/bin/python3
""" Declaration of class that inherits from a list"""


class MyList(list):
    """ Declaration of the function"""
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        print(sorted(self))
