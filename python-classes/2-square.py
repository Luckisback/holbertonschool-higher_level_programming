#!/usr/bin/python3
""" Creation of a Class called Square """


class Square:
    """ Definition of class Square """
    def __init__(self, size: int = 0):
        if type(size) != int:
            raise typeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
