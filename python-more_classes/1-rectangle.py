#!/usr/bin/python3
""" Creation of a class Rectangle that defines a
    rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """Definition de Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """managment of the property width"""
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    def height(self, value):
        """managment of the property Hight"""
        if isinstance(value, int):
            self.__height = vlaue
	else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
