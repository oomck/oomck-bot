# Class used to load the data for the chat-bot into ElasticSearch.

import json

from elasticsearch import Elasticsearch, helpers
from elasticsearch.helpers import BulkIndexError


es = Elasticsearch()

# Constants
data = "data/data.json"
index = "my-index"


# Method to load the data from JSON file.
def load_json_data():
    with open(data, 'r') as file:
        return json.load(file)


# Method to insert the data from the JSON file into ElasticSearch.
def insert_data_by_bulk(_data):
    try:
        helpers.bulk(es, _data, index=index)
    except BulkIndexError:
        print("Please increase your docker partition. This error occurs when there is not enough space to upload the "
              "rest of the data to the Docker ElasticSearch container.")


# Method to delete all the data from ElasticSearch.
def delete_data():
    es.indices.delete(index)


# Main method that utilizes the above methods to insert the data, and search for a specific instance in ElasticSearch.
if __name__ == "__main__":
    ubuntu_data = load_json_data()
    insert_data_by_bulk(ubuntu_data)
