from text_parser import Parser


class Bot:

    def __init__(self, elastic_client):
        self.parser = Parser()
        self.elastic = elastic_client
        print("Welcome to the UBUNTU help bot! What can I help you with?")

    def _elastic_search(self, query):
        return ""  # self.elastic.search(index="test", body={"query": {"match_all": {}}})

    def get_input(self):
        user_input = input("[You]: ")
        return self.parser.parse(user_input)

    def get_answer(self, user_input):
        response = self._elastic_search(user_input)
        print("response")
