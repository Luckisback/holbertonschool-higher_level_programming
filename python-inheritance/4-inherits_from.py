#!/usr/bin/python3
""" Declaration of a fucntion """


def inherits_from(obj, a_class):
    """ A function that find the kind of type the class """
    if not type(obj) == a_class and isinstance(obj, a_class):
        return True
    else:
        return False
