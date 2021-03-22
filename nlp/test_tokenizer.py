import unittest

from .tokenizer import Tokenizer


class TestTokenizer(unittest.TestCase):
    def test_tokenize(self):
        self.assertEqual(Tokenizer.tokenize("Hello, My name is Mike OXLONG!"), ["hello", "name", "mike", "oxlong"])

    # TODO: add tests for all the functionalities
