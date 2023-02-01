#!/usr/bin/python3
""" Creation of of a class called Square """


class Square:
    """Definition of the Class Square """
    def __init__(self, size: int = 0):
        if type(size) != int or type(size) is None:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Definition of a public instance methode
            @param seilf: the current instance
            @Return: returns the current area
        """
        return (self.__size) ** 2
