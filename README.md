# Oomck-Bot

## Getting Started

### Dependencies

- [Docker](https://www.docker.com/get-started)
- [Python 3](https://www.python.org/downloads/)

### Setup Project
1. Ensure that [Docker](https://www.docker.com/get-started) is currently running on your machine with an up-to-date version.
1. Install python dependencies with: `pip install -r requirements.txt`
1. Run `docker-compose up` to start elastic search.
1. In a new terminal, run `python main.py` which will start the elastic search container.
1. Type "load_data" to the bot to load the data into elastic search.
1. Type "exit" to end the chat with the bot.
1. Enjoy!

### Test
1. run `python -m unittest` to run all the tests

### Assignment 3 - Features
1. GUI:
    - We implemented a GUI to improve the overall experience for our users.
2. POS Tagging:
    - We implemented POS tagging to assign labels to tokens in the user's input. This helps improve the quality of the bot's responses.
3. Named Entity Recognition: 
    - We implemented this in our bot to help distinguish key elements within the user's input. This will help determine names of the characters and movies to improve the bot's understanding of message sent by the user.
4. Interaction with Another Bot via Sockets 
   - We connected our bot with another group's chatbot through sockets in order to allow communication between the two bots.
5. Automated Unit Testing: 
   - Unit tests were implemented to ensure that the quality of our code is maintained throughout the development process. This ensures that our bot behaves as expected at all times.
6. Handle Spelling Errors: 
   - This was implemented to ensure that there are no spelling mistakes in the user's input that could affect the quality of the response returned by the bot.
