#!/usr/bin/python3
""" Creation of a class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The class Rectangle """
    def __init__(self, width, height):
        """ A method for instentiation of attributs """
        if (width > 0 and height > 0) and
            (type(width) is int and type(heigth) is int) :
            self.__width = width
            self.__height = height
        else if type(width) != int:
            raise TypeError("width must be an integer")
        else if type(heigth) != int:
            raise TypeError("heigth must be an integer")
	else if width == 0:
            raise ValueError("width must be greater than 0")
        else if heigth == 0:
            raise ValueError("heigth must be greater than 0")

