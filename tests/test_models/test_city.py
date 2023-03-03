#!/usr/bin/python3
"""Unittest Module for City class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """testing the correct functioning of the class"""
    def test_attr(self):
        """test attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
