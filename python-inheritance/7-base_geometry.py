#!/usr/bin/python3
""" Creation of a class BaseGeometry """


class BaseGeometry:
    """ A classe that raise with an exception """
    def area(self):
        """ A function as method to raise """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ A methode that checks if Int """
        if type(name) is str:
            if type(value) != int:
                raise TypeError("<name> must be an integer")
            if value <= 0:
                raise ValueError("<name> must be greater than 0")
