class Cleaner:
    """
    A cleaner class that cleans a string to computer readable level
    """

    @staticmethod
    def clean(string):
        string = Cleaner.to_lower(string)
        string = Cleaner.fix_contractions(string)
        string = Cleaner.remove_punctuation(string)
        string = Cleaner.remove_stop_words(string)
        return string

    @staticmethod
    def to_lower(string):
        """
        :param string:
        :return: convert all the letters to lower case
        """
        return string.lower()

    @staticmethod
    def fix_contractions(string):
        """
        :param string:
        :return: fix all the contraction in a string
        """
        raise NotImplementedError()

    @staticmethod
    def remove_punctuation(string):
        """
        :param string:
        :return: remove all the punctuations from a string
        """
        raise NotImplementedError()

    @staticmethod
    def remove_stop_words(string):
        """
        :param string:
        :return: remove all the stop words from a sentence
        """
        raise NotImplementedError()

    # TODO: add extra methods
