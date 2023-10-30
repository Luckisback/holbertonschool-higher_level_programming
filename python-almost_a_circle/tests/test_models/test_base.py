#!/usr/bin/python3
""" Class Base's Unittest"""

import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """ Preparation of the test"""
    def test__init__(self):
        """Instance, and id attribut test"""
        b = Base()
        self.assertEqual(b.id, 1)

        b1 = Base()
        self.assertEqual(b1.id, 2)

        b2 = Base(25)
        self.assertEqual(b2.id, 25)

        b3 = Base()
        self.assertIsInstance(b3, Base)
        self.assertIsNotNone(b3.id)
        self.assertIsInstance(b3.id, int)
        self.assertNotIsInstance(b3.id, str)
