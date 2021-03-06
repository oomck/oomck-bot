import re


class Bot:

    def __init__(self, parser, elasticsearch):
        self.parser = parser
        self.elasticsearch = elasticsearch

    def _elastic_search(self, query):
        return \
            self.elasticsearch.search(index="fast_and_furious", body={"query": {"match": {"prompt": query}}}, size=1)[
                "hits"]["hits"]

    def get_input(self):
        user_input = input("[YOU]: ")
        parsed_input = self.parser.parse(user_input)
        return parsed_input

    def get_answer(self, user_input):
        elastic_query = self._elastic_search(user_input)
        if len(elastic_query) == 0:
            print("[BOT]: Sorry, I don't get what you're saying, can you try again?")
        else:
            for num, doc in enumerate(elastic_query):
                for key, value in doc.items():
                    if key == "_source":
                        print("[BOT]:", value['response'])
