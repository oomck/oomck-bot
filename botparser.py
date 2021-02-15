from autocorrect import Speller
import string


class BotParser:

    def __init__(self):
        with open('stop.txt') as input_file:
            self.stop_list = long_list = [line.strip() for line in input_file]

    def _tokenize(self, user_input):
        return user_input.split()

    def _normalize(self, user_input):
        return user_input.lower()

    def _remove_punctuation(self, user_input):
        # user_input.translate(str.maketrans('', '', string.punctuation))
        # return user_input
        for punctuation in string.punctuation:
            user_input = user_input.replace(punctuation, "")
        return user_input

    def _stop_filter(self, user_input):
        if len(user_input) == 1:
            return True
        for stop in self.stop_list:
            if user_input == stop:
                return True
        return False

    def _spell_check(self, word):
        spell = Speller()
        return spell(word)

    def parse(self, user_input):
        keywords_dict = {}
        # get list of user input
        user_input_list = self._tokenize(self._normalize(user_input))
        # recursively get dictionary
        return self._parse_input(user_input_list, keywords_dict, False, "")

    def _parse_input(self, user_input_list, keywords_dict, has_key_word, keyword):
        try:
            user_input = user_input_list[0]
        except IndexError:
            return keywords_dict
        # eliminate punctuation and spell check word
        user_input = self._spell_check(self._remove_punctuation(user_input))
        # check if word is unneeded, if it is continue to next word
        if not self._stop_filter(user_input):
            if not has_key_word:
                # mark word as key word
                keyword = user_input
                if keywords_dict.get(keyword) is None:
                    keywords_dict[keyword] = []
                has_key_word = True
            else:
                # insert word into keyword dictionary
                keywords_dict[keyword].append(user_input)
                has_key_word = False
        user_input_list.pop(0)
        return self._parse_input(user_input_list, keywords_dict, has_key_word, keyword)
