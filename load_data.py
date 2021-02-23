# Class used to load the data for the chat-bot into ElasticSearch.

import json

from elasticsearch import Elasticsearch, helpers

from search_data import search_by_index_and_id

es = Elasticsearch()


# Method to load the data from JSON file.
def load_json_data():
    with open("test_data.json") as file:
        return json.load(file)


# Method to insert the data from the JSON file into ElasticSearch.
def insert_data_by_bulk(data):
    response = helpers.bulk(es, data)
    print(response)


# Method to delete all the data from ElasticSearch.
def delete_data():
    es.indices.delete("test-index")


# Main method that utilizes the above methods to insert the data, and search for a specific instance in ElasticSearch.
if __name__ == "__main__":
    demo_data = load_json_data()
    insert_data_by_bulk(demo_data)
    res = search_by_index_and_id("test-index", 1)
    print(res)

