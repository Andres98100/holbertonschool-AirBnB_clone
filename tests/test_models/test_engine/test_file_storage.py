#!/usr/bin/python3
"""Unittest module class FileStorage"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage
"""import"""


class Test_file_storage(unittest.TestCase):
    
    def test_creation(self):
        """method test created"""
        self.assertIsInstance(storage, FileStorage)

if __name__ == "__main__":
    unittest.main()
