

class Tokenizer:
    """
    A tokenizer class that process a string to find
    important tokens in it
    """

    @staticmethod
    def tokenize(raw_input_string):
        """
        :param raw_input_string: A sentence as string
        :return: List of important tokens in raw_input_string
        """
        return raw_input_string.split()
