#!/usr/bin/python3
from models.rectangle import Rectangle
""""
ARGS:
    Square: The class the Inherits from Rectangle
    size: the attribue the will inherits the value of width and height
    x, y: quadrilateral coordinates
    id : id number for a geometric figure
"""


class Square(Rectangle):
    """The class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialisation of the instance's attributs"""

        super().__init__(size, size, x, y, id)
        """Calling the class parent with it's attributs"""

        self.size = size
        self.x = x
        self.y = y
        self.id = id

    def __str__(self):
        """The method the return"""
        return "[Square] ({}) {}/{} - {}".format(id, self.x, self.y, self.size)
