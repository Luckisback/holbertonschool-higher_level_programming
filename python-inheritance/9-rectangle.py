#!/usr/bin/python3
""" Creation of a Class called Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectancle inherits basegeometry"""

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Description rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
