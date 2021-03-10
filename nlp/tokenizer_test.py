import unittest

from .tokenizer import Tokenizer


class TokenizerTest(unittest.TestCase):
    def tokenize_test(self):
        self.assertEqual(Tokenizer.tokenize("Hello, My name is Mike OXLONG!"), ["hello", "name", "mike", "oxlong"])

    # TODO: add tests for all the functionalities
