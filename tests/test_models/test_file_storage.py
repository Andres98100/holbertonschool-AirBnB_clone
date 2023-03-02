#!/usr/bin/python3
"""Unittest for FileStorage class"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """Sets the class/obj"""
        cls.storage = FileStorage()
        try:
            os.rename(FileStorage._FileStorage__file_path, "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Removes JSON file after testing the other methods"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except Exception:
            pass
        try:
            os.rename("test_file.json", FileStorage._FileStorage__file_path)
        except Exception:
            pass

    def test_all(self):
        """Test case for 'all' method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test case for 'new' method"""
        model = BaseModel()
        self.storage.new(model)
        key = model.__class__.__name__ + "." + model.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test case for 'save' method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        """Test case for 'reload' method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        key = model.__class__.__name__ + "." + model.id
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
