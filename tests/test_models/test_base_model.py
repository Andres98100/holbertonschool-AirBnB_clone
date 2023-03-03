#!/usr/bin/python3
"""import"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Sets the class/obj"""
        cls.base_model = BaseModel()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    def test_save_method(self):
        """Test save method"""
        base1 = BaseModel()
        update = base1.updated_at
        base1.save()
        self.assertLess(update, base1.updated_at)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.base_model.__class__.__name__)
        obj_dict = str(self.base_model.__dict__)
        obj_str = f"[{cls_name}] ({self.base_model.id}) {obj_dict}"
        self.assertEqual(obj_str, self.base_model.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.base_model.id,
            "__class__": self.base_model.__class__.__name__,
            "created_at": self.base_model.created_at.isoformat(),
            "updated_at": self.base_model.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.base_model.to_dict())


if __name__ == "__main__":
    unittest.main()
