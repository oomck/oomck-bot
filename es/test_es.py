import unittest

from es import ElasticSearch


class TestES(unittest.TestCase):
    def test_es_running(self):
        try:
            ElasticSearch.ensure_running()
        except:
            self.fail("Elastic Search is not running")
