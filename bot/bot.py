from es import ElasticSearch
from nlp.cleaner import Cleaner


class Bot:
    """
    The main bot class
    """

    def __init__(self):
        self.cleaner = Cleaner
        self.es = ElasticSearch

    def ask(self, raw_input_string):
        """
        :param raw_input_string: Users question as raw string
        :return: Bots response as string
        """
        query = self.cleaner.clean(raw_input_string)
        results = self.es.search(query)

        if len(results) > 0:
            return results[0]["_source"]['response']

        return "Sorry, I don't get what you're saying, can you try again?"
