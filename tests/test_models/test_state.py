#!/usr/bin/python3
"""Unittest Module for State class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """testing the correct functioning of the class"""
    def test_attr(self):
        """test attributes"""
        state = State()
        self.assertEqual(state.name, "")

    def test_instance(self):
        """test is instance"""
        state = State()
        self.assertIsInstance(state, State)

    def test_type_attr(self):
        """test type attributes"""
        state = State()
        self.assertIsInstance(state.name, str)


if __name__ == '__main__':
    unittest.main()
