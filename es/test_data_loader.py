import unittest

from es.data_loader import DataLoader


class TestDataLoader(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_loader = DataLoader()

    def test_clear_data(self):
        try:
            self.data_loader.clear_data()
        except:
            self.fail("Could not clear elastic search")

    def test_load_data(self):
        try:
            self.data_loader.load_data()
        except:
            self.fail("Could not load data")
