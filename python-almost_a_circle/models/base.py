#!/usr/bin/python3
""" 
Base Class

Args:
    Base: First class
    __nb_objects: the private class attribut
    id: A public instance attribut    
"""

class Base:
    """ The first class called base """

    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
