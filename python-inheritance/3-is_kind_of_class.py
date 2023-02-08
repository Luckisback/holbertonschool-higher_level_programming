#!/usr/bin/python3
"""Declation of a function that checks a kind of class"""


def is_kind_of_class(obj, a_class):
    """ the function is_kind_of_class """
    return (True if type(obj) is a_class or
            isinstance(obj, a_class) else False)
