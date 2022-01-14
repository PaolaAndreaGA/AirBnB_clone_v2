#!/usr/bin/python3
""" Tests for amenity class"""
import unittest
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """ Define tests for Amenity class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(str(new.name)), str)
