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
        """assign the class"""
        self.obj = BaseModel()
    """method save"""
    def test_save(self):
        """Test that save updates the updated_at attribute"""
        original_updated_at = self.obj.updated_at
        self.obj.save()
        new_updated_at = self.obj.updated_at
        self.assertGreater(new_updated_at, original_updated_at)
    """"method str"""
    def test_str(self):
        """test str"""
        string = f"[{self.obj.__class__.__name__}] ({self.obj.id}) {self.obj.__dict__}"
        self.assertEquals(string, self.obj.__str__())
    """method to_dict"""
    def test_dict(self):
        """test dict"""
        original = self.obj.to_dict()
        new = self.obj.to_dict()
        self.assertEquals(original, new)

if __name__ == "__main__":
    unittest.main()
