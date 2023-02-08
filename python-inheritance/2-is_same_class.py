#!/usr/bin/python3
""" Declaration of a function that check type of an instance"""


def is_same_class(obj, a_class):
    """ Defintion of the class is_same_class """
    if type(obj) is a_class:
        return True
    else:
        return False
