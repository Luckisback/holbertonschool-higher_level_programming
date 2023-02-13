#!/usr/bin/python3
"""Creation of the a class"""


class Base:
    """ the class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ definition of a methode """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
