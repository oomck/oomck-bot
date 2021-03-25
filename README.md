# Oomck-Bot

## Getting Started

### Dependencies

- [Docker](https://www.docker.com/get-started)
- [Python 3](https://www.python.org/downloads/)

### Setup Project

1. Ensure that [Docker](https://www.docker.com/get-started) is currently running on your machine with an up-to-date version.
2. Install python dependencies with: `pip install -r requirements.txt`
3. Run `docker-compose up` to start elastic search.
4. In a new terminal, run `python main.py`.
5. Enjoy!

### Test

1. run `python -m unittest` to run all the tests

### Run sockets with other bot

1. Install python dependencies with: `pip install -r requirements.txt`.
2. Run `docker-compose up` to start elastic search.
3. Set the host address and port at the top of `python sockets/main.py`.
4. In a new terminal, run `python sockets/main.py` when the other bot is running as host.
