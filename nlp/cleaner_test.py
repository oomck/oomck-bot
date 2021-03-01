import unittest

from .cleaner import Cleaner


class TestCleaner(unittest.TestCase):
    def test_lower(self):
        self.assertEqual(Cleaner.to_lower("Hello My name is Mike OXLONG"), "hello my name is mike oxlong")

    # TODO: add tests for all the functionality
