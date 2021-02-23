from elasticsearch import Elasticsearch

es = Elasticsearch()


# Method for searching for a record in ElasticSearch with the index and id.
def search_by_index_and_id(_index, _id):
    res = es.get(
        index=_index,
        id=_id)
    return res
