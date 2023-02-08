#!/usr/bin/python3
""" Creation of a class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The class Rectangle """
    def __init__(self, width, height):
        """ A method for instentiation of attributs """
        if width >= 0 or height >= 0:
            self.__width = width
            self.__height = height
