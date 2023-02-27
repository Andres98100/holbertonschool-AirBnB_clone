#!/usr/bin/python3
"""import"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
"""class"""


class Test_base_model(unittest.TestCase):
    """method test save"""
    def test_creation(self):
        """test"""
        obj = BaseModel()
        self.assertEqual(datetime, type(obj.updated_at))
    """method """
if __name__ == "__main__":
    unittest.main()
