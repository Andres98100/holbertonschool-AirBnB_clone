#!/usr/bin/python3
"""import"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
"""class"""


class Test_base_model(unittest.TestCase):
    """method test created"""
    def test_creation(self):
        """test"""
        obj = BaseModel()
        self.assertEqual(datetime, type(obj.updated_at))
    """method to_dict"""
    def test_save(self):
        """test"""
        obj = BaseModel()
        obj.save()
        self.assertIsInstance(obj.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
