#!/usr/bin/python3
"""Unittest Module for Amenity class"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """testing the correct functioning of the class"""
    def test_name(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
