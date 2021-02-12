class Bot:
    # Prompt user and split string into list of words
    def prompt_user(self, prompt):
        test = input(prompt + "\n").split("/[^A-Za-z]/g")
        self.process_input(test)

    # Process string list input
    def process_input(self, input):
        print(input)
