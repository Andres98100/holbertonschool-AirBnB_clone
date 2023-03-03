#!/usr/bin/python3
"""Unittest Module for Review class"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """testing the correct functioning of the class"""
    def test_attr(self):
        """test attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_instance(self):
        """test is instance"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_type_attr(self):
        """test type attributes"""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)


if __name__ == '__main__':
    unittest.main()
