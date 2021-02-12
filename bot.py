import re


class Bot:
    # Prompt user and split string into list of words
    def prompt_user(self, prompt):
        return input(prompt + "\n")

    # Process string list input
    def process_input(self, input):
        # Split by spaces/symbols and remove empty strings
        result = list(filter(None, re.split("[^A-Za-z]", input)))
        return result
