from autocorrect import Speller
import string


class Parser:

    def __init__(self):
        with open('stop.txt') as input_file:
            self.stop_list = long_list = [line.strip() for line in input_file]
        self.spell = Speller()

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
        return self.spell(word)

    def parse(self, user_input):
        parsed_input = []
        # tokenize and normalize to get list of user input
        user_input_list = self._tokenize(self._normalize(user_input))
        # recursively get parsed input
        return " ".join(self._parse_input(user_input_list, parsed_input))

    def _parse_input(self, user_input_list, parsed_input):
        try:
            user_input = user_input_list[0]
        except IndexError:
            return parsed_input
        # eliminate punctuation and spell check word
        user_input = self._spell_check(self._remove_punctuation(user_input))
        # check if word is unneeded, if it is continue to next word
        if not self._stop_filter(user_input):
            parsed_input.append(user_input)
        user_input_list.pop(0)
        return self._parse_input(user_input_list, parsed_input)
