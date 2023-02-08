#!/usr/bin/python3
""" Declaration of a function that check type of an instance"""
def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
