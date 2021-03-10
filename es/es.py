from elasticsearch import Elasticsearch, helpers

import settings


class _ElasticSearch:
    """
    An intermediate DAO to interact with elastic search
    """

    def __init__(self):
        self.es = Elasticsearch(
            [settings.ES_URL],
            timeout=settings.ES_TIMEOUT,
            retry_on_timeout=settings.ES_RETRY_ON_TIMEOUT
        )

    def ensure_running(self):
        """
        Wait until elastic search is running or timeout
        :return:
        """
        self.es.cluster.health(wait_for_status="yellow", timeout="50s")

    def index_bulk(self, data):
        """
        :param data: an array of (prompt, response, tokens)
        :return:
        """
        helpers.bulk(self.es, data, index=settings.ES_INDEX_NAME)

    def clear_data(self):
        self.es.indices.delete(settings.ES_INDEX_NAME)

    def search(self, query):
        """
        Search in elastic search to find the best response that matches the tokens provided
        :param query:
        :return:
        """
        return self.es.search(
            index=settings.ES_INDEX_NAME,
            body={
                "query": {
                    "match": {
                        "prompt": query
                    }
                }
            },
            size=1
        )["hits"]["hits"]


ElasticSearch = _ElasticSearch()
