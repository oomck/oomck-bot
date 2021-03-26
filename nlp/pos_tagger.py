import nltk
from nltk import pos_tag
nltk.download('averaged_perceptron_tagger', quiet=True)


class POSTagger:
    """
    A class that processes tokenized words and attaches the associated part-of-speech
    """

    @staticmethod
    def tag(tokenized_input):
        """
        :param tokenized_input: A list of tokenized words
        :return: List of tagged pos words
        """
        return pos_tag(tokenized_input)
