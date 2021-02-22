# oomck-bot

## Getting started

### Dependancies

- [Docker](https://www.docker.com/get-started)
- [Python 3](https://www.python.org/downloads/)

### Setup Environment

1. Ensure that docker is curently running on your machine.
2. Install python dependencies with: `pip install -r requirements.txt`
3. Setup Kaggle API key by going to your kaggle Profile > Account > Create New API Token and downloading the `kaggle.json` to `~/.kaggle/kaggle.json`
4. Start the ElasticSearch container with: `./init.sh`.
5. Run the python init script with: `python init.py`.
