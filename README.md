# oomck-bot

## Getting started

### Dependancies

- [Docker](https://www.docker.com/get-started)
- [Python 3](https://www.python.org/downloads/)

### Setup Environment

1. Ensure that docker is curently running on your machine.
2. Install python dependencies with: `pip install -r requirements.txt`
3. Download [data.json](https://drive.google.com/file/d/137MJNQTUUswp4bv_Y8368o5lzAbW8y52/view?usp=sharing) and place in `data/data.json`
4. Start the ElasticSearch container with: `./init.sh`.
5. Run the python load_data script with `python load_data.py`. This only needs to be done once on your initial setup.
6. Run the python init script with: `python init.py`.
