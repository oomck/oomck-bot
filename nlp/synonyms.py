import nltk
from nltk.corpus import wordnet
nltk.download('wordnet', quiet=True)


class Synonyms:
    """
    A class that processes words and attaches the associated synonyms
    """

    @staticmethod
    def measure(user_input):
        """
        :param user_input: A word
        :return: List of synonyms
        """
        synonyms = []
        for synonym in wordnet.synsets(user_input):
            for lemma in synonym.lemmas():
                if lemma.name() not in synonyms:
                    synonyms.append(lemma.name())
        return synonyms
