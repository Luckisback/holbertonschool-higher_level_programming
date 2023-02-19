#!/usr/bin/python3
"""
    Update of the classe Rectangle"
"""


class Rectangle:
    """
        Déclaration of le Class Rectangle
    """

    def __init__(self, width=0, height=0):
        """ Initialization of a new instance """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the width proprety """

        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width proprety """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ get the height proprety """

        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height proprety """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Returns area of the rectangle """

        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns perimeter of the rectangle """

        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__width + self.__height)
