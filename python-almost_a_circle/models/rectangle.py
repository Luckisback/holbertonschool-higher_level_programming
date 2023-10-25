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

# Stting of the behavior of the Rectangle instance attribute

    """ definition of width as an object's property"""
    @property
    def width(self):
        return self.__width

    """ definition of, How width should act"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    """ definition of height as an object's property"""
    @property
    def height(self):
        return self.__height
    
    """ definition of, How height should act"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        
    """ definition of 'x' as an object's property"""
    @property
    def x(self):
        return self.__x

    """ definition of, How 'x' should act"""
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    """ definition of 'y' as an object's property"""
    @property
    def y(self):
        return self.__y

    """ definition of, How 'y' should act"""
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value