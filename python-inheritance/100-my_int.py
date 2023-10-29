#!/usr/bin/python3
"""The class that inherites from int"""


class MyInt(int):
    """class child of Int"""

    def __eq__(self, other):
        """definition of the operator '=' """

        return (not super().__eq__(other))

    def __ne__(self, other):
        """defintion of thr opérator '!=' """

        return (not super().__ne__(other))
