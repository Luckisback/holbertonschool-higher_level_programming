#!/usr/bin/python3
""" Declaration of class that inherits from a list"""


class MyList(list):
    """Created class inherits list"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Print self"""

        print(sorted(self))
