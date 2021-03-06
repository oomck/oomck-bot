# Class used to load the data for the chat-bot into ElasticSearch.

import json

from elasticsearch import Elasticsearch, helpers
from elasticsearch.helpers import BulkIndexError

# The load data script that is utilized in order to setup the Docker volume.
es = Elasticsearch(["localhost:9200"], timeout=30, retry_on_timeout=True)

# Constants
json_data = "../data/data.json"
index = "fast_and_furious"


# Method to load the data from JSON file.
def load_json_data():
    with open(json_data, 'r') as file:
        return json.load(file)


# Method to insert the data from the JSON file into ElasticSearch.
def insert_data_by_bulk(_data):
    try:
        print("Importing Data into ElasticSearch...")
        helpers.bulk(es, _data, index=index)
        print("Import Finished")
    except BulkIndexError:
        print("Please increase your docker partition. This error occurs when there is not enough space to upload the "
              "rest of the data to the Docker ElasticSearch container.")


# Method to delete all the data from ElasticSearch.
def delete_data():
    es.indices.delete(index)


# Main method that utilizes the above methods to insert the data, and search for a specific instance in ElasticSearch.
if __name__ == "__main__":
    # delete_data()
    fast_and_furious = load_json_data()
    insert_data_by_bulk(fast_and_furious)
