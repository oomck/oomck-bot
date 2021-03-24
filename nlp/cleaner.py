import string

import settings
from nlp.tokenizer import Tokenizer
from autocorrect import Speller


# TODO: use nltk
class Cleaner:
    """
    A cleaner class that cleans a string to computer readable level
    """

    tokenizer = Tokenizer()
    speller = Speller()

    @staticmethod
    def clean(query):
        query = Cleaner.to_lower(query)
        query = Cleaner.fix_contractions(query)
        query = Cleaner.remove_punctuation(query)

        tokens = Cleaner.tokenizer.tokenize(query)
        tokens = Cleaner.spell_check(tokens)
        tokens = Cleaner.remove_stop_words(tokens)

        return " ".join(tokens)

    @staticmethod
    def spell_check(tokens):
        return [Cleaner.speller(x) for x in tokens]

    @staticmethod
    def to_lower(query):
        """
        :param query:
        :return: convert all the letters to lower case
        """
        return query.lower()

    @staticmethod
    def fix_contractions(query):
        """
        :param query:
        :return: fix all the contraction in a string
        """
        return query

    @staticmethod
    def remove_punctuation(query):
        """
        :param query:
        :return: remove all the punctuations from a string
        """
        for punctuation in string.punctuation:
            query = query.replace(punctuation, " ")
        return query

    @staticmethod
    def remove_stop_words(tokens):
        """
        :param tokens:
        :return: remove all the stop words from a sentence
        """
        with open(settings.STOP_WORDS_URL) as input_file:
            stops = [line.strip() for line in input_file]
            return [x for x in tokens if x not in stops]
