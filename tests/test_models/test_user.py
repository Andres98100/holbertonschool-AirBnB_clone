#!/usr/bin/python3
"""Unittest Module for User class"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """testing the correct functioning of the class"""
    def test_email(self):
        user_email = User().email
        user_password = User().password
    def test_email(self):
        User().email
        self.assertEqual(User().email, "")
    pass
