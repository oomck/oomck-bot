import json

import settings
from . import ElasticSearch


class DataLoader:
    def read_json_data(self):
        """
        Read the data from json file
        :return:
        """
        with open(settings.DATA_URL, 'r') as file:
            return json.load(file)

    def load_data(self):
        """
        Delete and Reload all the data in elastic search
        :return:
        """
        self.clear_data()
        ElasticSearch.index_bulk(self.read_json_data())

    def clear_data(self):
        """
        Clear the elastic search index
        :return:
        """
        ElasticSearch.clear_data()
