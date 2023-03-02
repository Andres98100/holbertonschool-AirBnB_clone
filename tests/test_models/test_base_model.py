#!/usr/bin/python3
"""import"""
import unittest
from models.base_model import BaseModel

import os


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Sets the class/obj"""
        cls.base_model = BaseModel()
        try:
            os.rename("file.json", "real.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
            os.rename("real.json", "file.json")
        except Exception:
            pass

    def test_save_method(self):
        from models import storage
        """Test case for 'save' method"""
        datetime_prev = self.base_model.updated_at
        self.base_model.save()
        self.assertGreater(self.base_model.updated_at, datetime_prev)
        self.assertIn(self.base_model, storage.all().values())

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