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
    """method getter"""
    def setUp(self):
        self.obj = BaseModel()
    """method save"""
    def test_save(self):
        """Test that save updates the updated_at attribute"""
        original_updated_at = self.obj.updated_at
        self.obj.save()
        new_updated_at = self.obj.updated_at
        self.assertGreater(new_updated_at, original_updated_at)

if __name__ == "__main__":
    unittest.main()
