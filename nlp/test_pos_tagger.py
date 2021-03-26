import unittest

from .pos_tagger import POSTagger


class TestPOSTagger(unittest.TestCase):
    def test_pos_tagger(self):
        self.assertEqual(
            POSTagger.tag(["My", "name", "is", "Mike", "OXLONG"]),
            [("My", "PRP$"), ("name", "NN"), ("is", "VBZ"), ("Mike", "NNP"), ("OXLONG", "NNP")]
        )
