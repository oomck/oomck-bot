

class ElasticSearch:
    """
    An intermediate DAO to interact with elastic search
    """

    def __init__(self):
        # TODO: ensure elastic search is up and running
        # TODO: ensure data is loaded
        pass

    def index(self, prompt, response, tokens):
        # Not sure if we need this
        raise NotImplementedError()

    def index_bulk(self, data):
        """
        :param data: an array of (prompt, response, tokens)
        :return:
        """
        raise NotImplementedError()

    def search(self, tokens):
        """
        Search in elastic search to find the best response that matches the tokens provided
        :param tokens:
        :return:
        """
        raise NotImplementedError()
