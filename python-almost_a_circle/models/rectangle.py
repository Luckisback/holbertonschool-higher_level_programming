#!/usr/bin/python3
""" 
Base Class

Args:
    Base: First class
    __nb_objects: the private class attribut
    id: A public instance attribut
    Rectangle: A classe inherite the classe Base
    __width, __height, __x, __y: Private instance attribute of Rectangle   
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

class Rectangle(Base):
    """ A classe inherite Base"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.__width = width
        self.__height = height
        __x = x
        __y = y

"""Stting of the behavior of the Rectangle instance attribute"""

@property
def width(self):
    """ definition of width as an object property"""
    return self.__width

@width.setter
def width(self, value):
    """ definition of, How width should act"""
    
    if not isinstance(value, int):
        raise ValueError("width must be an integer")
    if value <= 0:
        raise ValueError("width must be greater than 0")
    self.__width = value