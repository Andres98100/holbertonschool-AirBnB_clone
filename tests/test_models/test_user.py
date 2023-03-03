#!/usr/bin/python3
"""Unittest Module for User class"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """testing the correct functioning of the class"""
    def test_str_attr(self):
        """test attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_str(self):
        """attribute type test"""
        user = User()
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)


if __name__ == "__main__":
    unittest.main()
