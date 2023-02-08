#!/usr/bin/python3
""" Creation of a class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The class Rectangle """
    def __init__(self, width, height):
        if ((width > 0 and height > 0) and
            (type(width) is int and type(height) is int)):
            self.__width = width
            self.__height = height
        elif type(width) is str:
            raise TypeError("width must be an integer")
        elif type(height) is str:
            raise TypeError("heigth must be an integer")
        elif width == 0:
            raise ValueError("width must be greater than 0")
        elif height == 0:
            raise ValueError("heigth must be greater than 0")
