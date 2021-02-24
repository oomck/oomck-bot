from elasticsearch import Elasticsearch

es = Elasticsearch()


# Method for searching for a record in ElasticSearch with the index and id.
def search_by_index_and_id(_index, _id):
    res = es.get(
        index=_index,
        id=_id)
    return res


if __name__ == "__main__":
    # Sample search of a record that is stored in ElasticSearch
    test = search_by_index_and_id("my-index", "Rwv90XcBgkIEUIpKU2XM")
    print(test)
