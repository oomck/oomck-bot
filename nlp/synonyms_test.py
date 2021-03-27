import unittest

from .synonyms import Synonyms


class TestSynonyms(unittest.TestCase):
    def test_pos_tagger(self):
        self.assertCountEqual(
            Synonyms.measure('active'),
            ['dynamic', 'fighting', 'combat-ready', 'active_voice', 'active_agent', 'participating', 'alive', 'active']
        )
