#!/usr/bin/python3
"""Unittest Module for User class"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """testing the correct functioning of the class"""
    def test_str_attr(self):
        user = User()
        self.assertEqual(User().email, "")
        self.assertEqual(User().password, "")
        self.assertEqual(User().first_name, "")
        self.assertEqual(User().last_name, "")
    def test_str(self):
        user = User()
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)

if __name__ == "__main__":
    unittest.main()
