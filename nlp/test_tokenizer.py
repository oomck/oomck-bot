import unittest

from .tokenizer import Tokenizer


class TestTokenizer(unittest.TestCase):
    def test_tokenize(self):
        self.assertEqual(
            Tokenizer.tokenize("Hello, My name is Mike OXLONG!"),
            ["Hello", ",", "My", "name", "is", "Mike", "OXLONG", "!"]
        )
