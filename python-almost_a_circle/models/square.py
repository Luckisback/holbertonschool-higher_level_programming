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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """That assigns an argument to each attribute"""
        if args:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                if i == 1:
                    self.size = v
                if i == 2:
                    self.x = v
                if i == 3:
                    self.y = v
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
